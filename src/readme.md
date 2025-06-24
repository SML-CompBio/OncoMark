# README

## Description
This folder contains various scripts and notebooks used in the preparation, training, validation, and analysis of the OncoMark model. Below is a detailed description of each file and its purpose:

---

### 1. **`Model_Train_Data_Prep.ipynb`**

* **Purpose**: Prepares and processes training data for model development. This includes feature extraction, label assignment, and dataset formatting.

---

### 2. **`Model_Train_and_Int_Val.ipynb`**

* **Purpose**:

  * Trains the OncoMark model.
  * Performs **five-fold cross-validation repeated twice** to ensure robust and consistent evaluation.

---

### 3. **`Model_Val_Ext_Syn_Data.ipynb`**

* **Purpose**:

  * Prepares five external validation datasets.
  * Runs the trained model on these datasets to generate predictions and evaluate generalizability.

---

### 4. **`Model_Val_Metastasis.ipynb`**

* **Purpose**:

  * Prepares primary site data from two datasets with confirmed metastasis.
  * Validates whether the model correctly identifies **Activation of Invasion and Metastasis** hallmark.

---

### 5. **`Model_Val_Normal_Cancer.ipynb`**

* **Purpose**:

  * Prepares and evaluates the model on six cancer datasets and two normal tissue datasets.
  * Assesses the model’s ability to differentiate between malignant and normal samples.

---

### 6. **`Model_Comparison.ipynb`**

* **Purpose**:

  * Compares OncoMark model performance against traditional ML models:

    * Logistic Regression
    * Decision Tree
    * Random Forest
    * Support Vector Classification (SVC)
    * Multi-Layer Perceptron (MLP)
    * XGBoost
  * Evaluation conducted on the same datasets used in `Model_Val_Normal_Cancer.ipynb`.

---

### 7. **`MTL.py`**

* **Purpose**:

  * Contains the full implementation of the **OncoMark model architecture**, based on **multi-task learning (MTL)** principles.

---

### 8. **`Drug_Analysis.ipynb`**

* **Purpose**:

  * Performs drug-response correlation analysis using hallmark activity scores.
  * Generates visualizations and results shown in **Figure 5** of the manuscript.

---

### 9. **`Stage_Analysis.ipynb`**

* **Purpose**:

  * Conducts co-association analysis between hallmark activity and **clinical staging** (AJCC/TNM).
  * Results are presented in **Figure 3**.

---

### 10. **`UCELL.R`**

* **Purpose**:

  * Contains code for calculating **hallmark signature scores** using the **UCell** method in R.
  * These scores are used as labels or validation metrics in model training and evaluation.

---

### 11. **`Label_Validation.ipynb`**

* **Purpose**:

  * Validates the **binary labels** assigned to hallmark activity using thresholding techniques.
  * Ensures consistency and biological relevance of the labeling strategy.

---

### 12. **`data_info.R`**

* **Purpose**:

  * Extract Mitochondrial Content and total count to faciliate data filtering.

---

## Usage
Each file is self-contained and should be executed in the specified order to reproduce results and analyses as per the OncoMark project. Refer to the accompanying documentation or comments within each file for additional guidance.
