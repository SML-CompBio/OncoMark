import tensorflow as tf
import joblib
import pandas as pd
import numpy as np
from scipy.stats import rankdata

def predict_hallmark_scores(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Process input data and predict hallmark scores using a pre-trained TensorFlow model included in the package.

    Parameters:
        input_df (pd.DataFrame): Input DataFrame containing the data to process and predict.

    Returns:
        pd.DataFrame: A DataFrame containing the predicted hallmark scores.
    """
    # Define paths to the local resources (same directory as this Python file)
    model_path = 'hallmark_model.keras'
    scaler_path = 'hallmark_scaler.joblib'
    feature_file = 'hallmark_feature.txt'

    # Load the pre-trained model and scaler
    model = tf.keras.models.load_model(model_path)
    scaler = joblib.load(scaler_path)

    # Load feature names
    with open(feature_file, 'r') as file:
        feature_names = file.read().splitlines()

    # Define hallmark tasks
    hall_list = ['AIM', 'DCE', 'EGS', 'GIM', 'RCD', 'SPS', 'AID', 'IA', 'ERI', 'TPI']

    # Process input DataFrame
    processed_df = input_df.loc[:, ~input_df.columns.duplicated(keep='first')]
    processed_df = processed_df.reindex(columns=feature_names, fill_value=0).fillna(0)

    # Rank and log-transform the data
    processed_df_index = processed_df.index
    ranked_data = rankdata(processed_df * -1, axis=1, method='average')
    log_transformed_data = np.log2(ranked_data)

    # Scale the data
    scaled_data = scaler.transform(log_transformed_data)

    # Predict hallmark scores
    predictions = model.predict(scaled_data)

    # Create a DataFrame for predictions
    prediction_df = pd.DataFrame()
    for task_id, hall_name in enumerate(hall_list):
        prediction_df[hall_name] = predictions[task_id].flatten()

    # Restore the original index
    prediction_df.index = processed_df_index

    return prediction_df