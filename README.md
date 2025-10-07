<div align="center">
  <img src="https://github.com/user-attachments/assets/e12bcab1-3856-4c11-bebe-6fe148dad1b2" alt="Oncomark Poster">
</div>
<br>

**OncoMark** is a deep learning tool designed to systematically quantify hallmark activity using transcriptomics data from routine tumor biopsies. Ideal for applications in oncology research, personalized medicine, and biomarker discovery.

---

## Documentation

Comprehensive documentation is available at:  
[OncoMark Documentation](https://oncomark.readthedocs.io/en/latest/)

---

## Installation

[![PyPI](https://badge.fury.io/py/OncoMark.svg)](https://pypi.org/project/OncoMark/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14647336.svg)](https://doi.org/10.5281/zenodo.14647336)
[![DOI](https://img.shields.io/badge/Dryad-DOI-orange)](https://doi.org/10.5061/dryad.zw3r228jc)

Install OncoMark using pip:

```bash
pip install OncoMark
```

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

[OncoMark Web Server](https://oncomark-ai.hf.space/)

---

## Suggestions

We welcome suggestions! If you have any ideas or feedback to improve OncoMark, please reach out to [Shreyansh Priyadarshi](mailto:shreyansh.priyadarshi02@gmail.com).

---

## Citation
```bibtex
Priyadarshi, S., Mazumder, C., Neekhra, B. et al. OncoMark: a high-throughput neural multi-task learning framework for comprehensive cancer hallmark quantification. Commun Biol 8, 1434 (2025). https://doi.org/10.1038/s42003-025-08727-z
