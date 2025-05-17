import streamlit as st
import pandas as pd
import numpy as np
import joblib
from scipy.stats import rankdata
import time
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import matplotlib.pyplot as plt
import io
from ulm import run_ulm
from mlm import run_mlm
from plotting import plot_barplot
import tensorflow as tf
import os

# Page Configuration
st.set_page_config(page_title="OncoMark", layout="wide")
st.image("oncomark_title.png", caption="", use_container_width=True)
# st.title("OncoMark")

# Sidebar for uploading data
st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your data file (CSV)", type=["csv"])
st.sidebar.markdown("[Need help? View tutorial](https://oncomark.readthedocs.io/en/latest/usage/)", unsafe_allow_html=True)

# Description and Instructions
# st.write("AI to predict cancer hallmarks from transcriptomics data.")

# Load model
model_path = 'hallmark_model.keras'
scaler_path = 'hallmark_scaler.joblib'
feature_file = 'hallmark_feature.txt'

# Load the pre-trained model and scaler
model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), model_path))
scaler = joblib.load(os.path.join(os.path.dirname(__file__), scaler_path))

# Load feature names
with open((os.path.join(os.path.dirname(__file__), feature_file)), 'r') as file:
    feature_names = file.read().splitlines()

# Define hallmark tasks
hall_list = ['AIM', 'DCE', 'EGS', 'GIM', 'RCD', 'SPS', 'AID', 'IA', 'ERI', 'TPI']
collectri = pd.read_csv('collectri_df.csv')
progeny = pd.read_csv('progeny_df.csv')

# Show an example structure if no data is uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, index_col=0)
    tf_acts, tf_pvals = run_ulm(mat=data, net=collectri, verbose=False)
    pathway_acts, pathway_pvals = run_mlm(mat=data, net=progeny, verbose=False)

    st.write("### Uploaded Data")
    st.write(data.iloc[:5, :50])
    data = data.loc[:, ~data.columns.duplicated(keep='first')]
    data = data.reindex(columns=feature_names, fill_value=0).fillna(0)
    data_index = data.index
    data = rankdata(data * -1, axis=1, method='average')
    data = np.log2(data)
    data = scaler.transform(data)
else:
    st.write("### Example Input Format")
    st.info("**Note:** I am flexible and can handle both normalized and non-normalized input data. Upload your data as is, and the model will adjust accordingly to provide accurate predictions.")
    raw_count_data = pd.DataFrame({
        'GeneA': [120, 150, 80],
        'GeneB': [200, 180, 190],
        'GeneC': [90, 75, 110],
        'GeneD': [60, 95, 100]
    }, index=['Sample1', 'Sample2', 'Sample3'])
    st.write(raw_count_data)

# Dummy model function (replace with actual model prediction)
def model_predict(input_data):
    predictions = model.predict(data)
    prediction_df = pd.DataFrame()
    for task_id, hall_name in enumerate(hall_list):
        prediction_df[hall_name] = predictions[task_id].flatten()
    prediction_df.index = data_index
    return prediction_df

def display_loading_animation():
    with st.empty():
        for i in range(3):
            st.write("🔍 Predicting" + "." * (i + 1))
            time.sleep(1.0)
        st.write("🚀 Almost there...")

# Initialize predictions to None
predictions = None

# Predict and display results if data is uploaded
if uploaded_file is not None:
    st.write("### Predictions")
    display_loading_animation()
    predictions = model_predict(data)
    predictions = predictions.reset_index()
    # st.write(predictions)
else:
    st.write("### Predictions")
    st.info("Upload your data to see predictions.")


selected = None

# Display analysis if predictions are available
if predictions is not None:
    # Display predictions in AgGrid
    gb = GridOptionsBuilder.from_dataframe(predictions)
    gb.configure_selection(selection_mode='single', use_checkbox=False)
    gb.configure_default_column(resizable=True, autoWidth=True, maxWidth=100)
    grid_options = gb.build()

    grid_response = AgGrid(
        predictions,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        height=300,
        enable_enterprise_modules=False,
        allow_unsafe_jscode=True,
        theme='streamlit',
        custom_css={
            ".ag-row-selected": {
                "background-color": "#90EE90 !important"
            }
        }
    )

    csv_grid = predictions.to_csv().encode('utf-8')
    st.download_button(
        label="Download Table as CSV",
        data=csv_grid,
        file_name='aggrid_table.csv',
        mime='text/csv'
    )

    # Extract selected row data and display bar plot on selection
    selected = grid_response['selected_rows']
    if selected is not None:
        st.write("### Analysis")
        selected_df = pd.DataFrame(selected)
        sample_name = selected_df['index'][0]

        st.write('##### Transcription factor activity')
        st.info('If it is positive, we interpret that the TF is active and if it is negative we interpret that it is inactive.')
        plot_barplot(
        acts=tf_acts,
        contrast=sample_name,
        top=50,
        vertical=False,
        figsize=(11, 5))
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=300)
        buf.seek(0)
        st.pyplot(plt)
        # Provide option to download the plot
        st.download_button(
            label="Download Plot as PNG",
            data=buf,
            file_name='tf_hallmark_{}.png'.format(sample_name),
            mime='image/png'
        )

        st.write('##### Pathway activity')
        st.info('If it is positive, we interpret that the pathway is active and if it is negative we interpret that it is inactive.')
        plot_barplot(
        pathway_acts,
        sample_name,
        top=50,
        vertical=False,
        figsize=(6, 3))
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=300)
        buf.seek(0)
        st.pyplot(plt)
        # Provide option to download the plot
        st.download_button(
            label="Download Plot as PNG",
            data=buf,
            file_name='pathway_hallmark_{}.png'.format(sample_name),
            mime='image/png'
        )

    else:
        st.write("### Analysis")
        st.info('Click on a sample under predictions to see the analysis')
else:
    st.write("### Analysis")
    st.info('Click on a sample under predictions to see the analysis')

# Footer
st.write("----")
st.markdown("[Visit our GitHub Repository](https://github.com/SML-CompBio/OncoMark)", unsafe_allow_html=True)

# Running the app: use `streamlit run filename.py`
