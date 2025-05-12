## Usage

OncoMark provides a Python API and a web interface to quantify hallmark activity from transcriptomics data. This page outlines how to use both interfaces effectively.

---

### Example Data

You can find example input data for testing in the `test` directory of the GitHub repository:

[OncoMark Test Data](https://github.com/SML-CompBio/OncoMark/blob/main/test/model_test_data.csv)

---

### Python API

The Python API allows you to directly process data and predict hallmark scores using the pre-trained model provided with the package.

#### Step 0: Install Packages

```bash
pip install OncoMark
```

#### Step 1: Import Required Libraries

Before using OncoMark, ensure you have your transcriptomics data in a pandas `DataFrame`.

```python
import pandas as pd
from OncoMark import predict_hallmark_scores
```

#### Step 2: Load Input Data

Load your transcriptomics data into a pandas `DataFrame`. The data should be formatted with samples as rows and genes as columns.

```python
# Load input data as a pandas DataFrame
input_data = pd.read_csv('path_to_your_data.csv', index_col=0)
```

#### Step 3: Predict Hallmark Scores

Use the `predict_hallmark_scores` function to process the data and generate hallmark activity predictions.

```python
# Predict hallmark scores
predictions = predict_hallmark_scores(input_data)

# Display the predictions
print(predictions)
```

#### Step 4: Save Results (Optional)

You can save the predictions as a CSV file for further analysis.

```python
# Save predictions to a CSV file
predictions.to_csv('predictions.csv')
```

---

### Web Interface

OncoMark also provides a user-friendly web interface for those who prefer not to write code.

You can use the hosted web server to upload your data and obtain hallmark activity predictions:

[OncoMark Web Server](https://oncomark-ai.hf.space/)

<div style="padding:42.86% 0 0 0;position:relative;">
  <iframe src="https://player.vimeo.com/video/1083623369?h=3bc9b08821&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" 
    frameborder="0" 
    allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" 
    style="position:absolute;top:0;left:0;width:100%;height:100%;" 
    title="OncoMark_Usage">
  </iframe>
</div>

<script src="https://player.vimeo.com/api/player.js"></script>

---

### Notes and Tips

- Ensure your input data contains genes matching the feature names used during model training.
- Ensure that the genes is in the columns of the datasets.
- Genes missing from the input data but used during model training will be filled with zeros, while additional genes not used in training will be ignored.
- Check the [Documentation](https://oncomark.readthedocs.io/en/latest/) for troubleshooting tips and advanced usage.

---

With this guide, you are ready to start exploring OncoMark's capabilities to quantify hallmark activity from your transcriptomics data.

---
