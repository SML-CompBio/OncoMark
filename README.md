<div align="center">
  <img src="https://github.com/user-attachments/assets/4da8fdff-41dd-49aa-b4f0-32ed1806a3bc" alt="Oncomark Poster">
</div>
<br>

**OncoMark** is a deep learning tool designed to systematically quantify hallmark activity using transcriptomics data from routine tumor biopsies. Ideal for applications in oncology research, personalized medicine, and biomarker discovery.

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

[OncoMark Web Server](https://oncomark-ai.hf.space/)

---

## Suggestions

We welcome suggestions! If you have any ideas or feedback to improve OncoMark, please reach out to [Shreyansh Priyadarshi](mailto:shreyansh.priyadarshi02@gmail.com).

---

## Citation
```bibtex
@article {Priyadarshi2025.02.03.636380,
	author = {Priyadarshi, Shreyansh and Mazumder, Camellia and Neekhra, Bhavesh and Biswas, Sayan and Chowdhury, Debojyoti and Gupta, Debayan and Haldar, Shubhasis},
	title = {Robust Prediction of Patient-Specific Cancer Hallmarks Using Neural Multi-Task Learning: a model development and validation study},
	elocation-id = {2025.02.03.636380},
	year = {2025},
	doi = {10.1101/2025.02.03.636380},
	publisher = {Cold Spring Harbor Laboratory},
	abstract = {Background Accurate quantification of cancer hallmark activity is essential for understanding tumor progression, tailoring treatments, and improving patient outcomes. Traditional methods, such as histopathological grading and immunohistochemistry for protein expression, often overlook the complex interplay between cancer cells and the tumor microenvironment and provide limited insight into hallmark-specific mechanisms. We aimed to develop OncoMark, a high-throughput deep learning-enabled neural multi-task learning framework capable of systematically quantifying integrative hallmarks activities using transcriptomics data from routine tumor biopsies.Methods In this study, we acquired single-cell transcriptomics data from 941 tumor samples across 14 tissue types, comprising nearly 3.1 million cells from 56 studies conducted worldwide, to form a large multicenter dataset. Our model employs a supervised neural multi-task learning method designed to predict multiple cancer hallmarks present in the biopsy samples simultaneously. The OncoMark model was developed and tested on 90\% of the studies (patients from 51 studies) using repeated five-fold cross-validation performed twice. For further evaluation, the model was assessed on the remaining 10\% of the studies (patients from 5 studies) that were excluded from the initial training and testing dataset. Additionally, we included patients from publicly available datasets, including TCGA, GTEx, ANTE, MET500, POG570, CCLE, TARGET, and PCAWG to validate the model{\textquoteright}s performance. The primary objective was to evaluate the performance of the model in identifying cancer hallmarks in cancer datasets and ensure no hallmark predictions were made in normal samples across the four prespecified groups: (i) internal test set, (ii) external test set, (iii) normal samples (real-world), and (iv) cancer samples (real-world).Findings OncoMark demonstrated exceptional performance in predicting cancer hallmark states, achieving near-perfect accuracy across internal test data and five external test datasets. Internal testing consistently showed accuracy, precision, recall, and F1 scores exceeding 99\%, underscoring the model{\textquoteright}s reliability across hallmarks. External test further confirmed these findings, with accuracy, precision, recall, F1 scores, and balanced accuracy consistently exceeding 96{\textperiodcentered}6\%, and multiple datasets achieving perfect scores, highlighting the model{\textquoteright}s exceptional generalizability and robustness. Specificity tests using GTEx and ANTE datasets accurately classified normal tissues, while sensitivity analysis on TCGA, MET500, CCLE, TARGET, PCAWG, and POG570 datasets effectively identified cancer hallmarks.Interpretation We developed an AI-based framework that enables accurate, efficient, and cost-effective quantification of cancer hallmark activity directly from transcriptomics data. The framework demonstrated significant potential as an assistive tool for guiding personalized treatment strategies and advancing the clinical management of cancer patients.Funding Ashoka University, S.N. Bose National Centre for Basic Sciences, Mphasis F1 Foundation, DST SERB Core Research Grant.Evidence before this study We conducted an extensive literature search using Google Scholar and PubMed without language restrictions, employing search terms such as {\textquotedblleft}(Predicting OR Classifying OR Annotating) and (cancer hallmarks) AND (Deep OR Machine Learning) OR (Artificial Intelligence OR AI).{\textquotedblright} While there have been advancements in molecular oncology and computational methodologies over the two decades since the concept of cancer hallmarks was first introduced, a comprehensive machine learning or deep learning framework to annotate all cancer hallmarks simultaneously from tumor biopsy samples remains to be developed. Additionally, the scarcity of hallmark-annotated datasets has posed a significant challenge, hindering the development of robust predictive models.Added value of this study This study introduces OncoMark, a novel high-throughput neural multi-task learning (N-MTL) framework designed to predict all cancer hallmark activities simultaneously from biopsy samples. OncoMark addresses the lack of annotated hallmark-specific data by generating synthetic biopsy (pseudo-bulk) datasets annotated with hallmark activity, meticulously modeled to reflect real-world tumor biology while maintaining clinical relevance. The framework employs a multi-task learning approach to capture interdependencies among hallmarks, advancing beyond isolated predictions to offer a holistic view of tumor biology. Validation on five independent datasets comprising 95 patient samples demonstrated its generalizability and reproducibility. Further external validation using eight datasets, encompassing over 11,679 cancer and 8348 normal patient samples, reinforced its robustness. To promote clinical integration, a user-friendly web-based tool was developed, enabling seamless access for oncologists and researchers.Implications of all the available evidence The OncoMark framework represents a transformative advancement in cancer diagnostics and treatment planning. By enabling accurate and reproducible prediction of all hallmark activities simultaneously from biopsy samples, this model paves the way for precision oncology at scale. Its ability to systematically capture hallmark interdependencies provides deeper insights into tumor behavior, guiding the development of individualized targeted therapies. The incorporation of a web-based interface ensures the accessibility of this innovation to clinicians worldwide, bridging the gap between computational oncology and clinical practice. Following further validation and integration into healthcare workflows, OncoMark has the potential to improve cancer outcomes by delivering timely, cost-effective, and precise tumor analyses, facilitating informed therapeutic decision-making with unparalleled precision.Cancer progression is driven by a set of well-defined biological principles{\textemdash}collectively termed the {\textquotedblleft}hallmarks of cancer{\textquotedblright}{\textemdash}yet current diagnostic approaches seldom incorporate these distinct molecular features into clinical practice. Despite substantial progress in molecular oncology, traditional methods like histopathological grading and immunohistochemical assays often fail to capture the complex interplay between cancer cells and the tumor microenvironment, emphasizing the need for robust computational frameworks capable of systematically quantifying hallmark-specific activity. Here, we address this gap by developing OncoMark, a high-throughput neural multi-task learning (N-MTL) framework designed to simultaneously quantify hallmark activities in tumor biopsies using transcriptomics data. We show that OncoMark achieves near-perfect accuracy, precision, recall, and F1 scores (\&gt;99\%) in cross-validation, with external validation consistently exceeding 96.6\% on five independent datasets. Further evaluation on eight additional datasets{\textemdash}including large-scale cancer cohorts (TCGA, MET500, CCLE, TARGET, PCAWG, POG570) and normal tissue datasets (GTEx, ANTE){\textemdash}demonstrated high specificity for normal samples and robust sensitivity for hallmark prediction in cancer. By delivering a comprehensive and cost-effective molecular portrait of tumor biology and providing a user-friendly web platform accessible at https://oncomark-ai.hf.space/, OncoMark has the potential to guide tailored treatment strategies and advance precision oncology. More broadly, this framework signifies a transformative step toward routine hallmark-based diagnostics, promising to improve patient outcomes by facilitating timely and precise tumor profiling.Competing Interest StatementThe authors have declared no competing interest.},
	URL = {https://www.biorxiv.org/content/early/2025/02/08/2025.02.03.636380},
	eprint = {https://www.biorxiv.org/content/early/2025/02/08/2025.02.03.636380.full.pdf},
	journal = {bioRxiv}
}
