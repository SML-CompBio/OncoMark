# OncoMark

**OncoMark** is a Python package designed to systematically quantify hallmark activity using transcriptomics data from routine tumor biopsies. Ideal for applications in oncology research, personalized medicine, and biomarker discovery.

---

## Installation

Install OncoMark using pip:

```bash
pip install OncoMark
```

---

## Documentation

Comprehensive documentation is available at:  
[OncoMark Documentation](https://oncomark.readthedocs.io/en/latest/)

---

## Usage

### Python API

```python
import pandas as pd
from OncoMark import predict_hallmark_scores

# Load input data as a pandas DataFrame. Genes must be in column.
input_data = pd.read_csv('input_data.csv', index_col=0)

# Predict hallmark scores
predictions = predict_hallmark_scores(input_data)

# Display the predictions
predictions
```

### Web Server

OncoMark also provides a web server for easy interaction.

#### Access the Online Web Server

You can use the hosted web server directly:

[OncoMark Web Server](https://iamspriyadarshi-oncomark.hf.space/)

---

## Contributors ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/iamspriyadarshi"><img src="https://avatars.githubusercontent.com/iamspriyadarshi" width="100px;" alt=""/><br /><sub><b>Shreyansh Priyadarshi</b></sub></a></td>
    <td align="center"><a href="https://github.com/iamcamellia"><img src="https://avatars.githubusercontent.com/iamcamellia" width="100px;" alt=""/><br /><sub><b>Camellia Mazumder</b></sub></a></td>
  </tr>
</table>

---

## Suggestions

We welcome suggestions! If you have any ideas or feedback to improve OncoMark, please reach out to [Shreyansh Priyadarshi](mailto:shreyansh.priyadarshi02@gmail.com).

---
