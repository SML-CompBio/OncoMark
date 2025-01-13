# README

## Description
This folder contains various scripts and notebooks used in the preparation, training, validation, and analysis of the OncoMark model. Below is a detailed description of each file and its purpose:

### 1. **Model_Train_Data_Prep.ipynb**
   - **Purpose**: Prepares the training data for model development.

### 2. **Model_Train_and_Int_Val.ipynb**
   - **Purpose**: 
     - Trains the model.
     - Performs five-fold cross-validation, repeated twice, to ensure robust evaluation.

### 3. **Model_Val_Ext_Syn_Data.ipynb**
   - **Purpose**: 
     - Prepares the five external validation datasets.
     - Generates model inferences on these datasets.

### 4. **Model_Val_Normal_Cancer.ipynb**
   - **Purpose**: 
     - Prepares data and validates the model on datasets containing six cancer types and two normal tissues.

### 5. **MTL.py**
   - **Purpose**: Contains the implementation of the OncoMark Model Architecture.

### 6. **Drug_Analysis.ipynb**
   - **Purpose**: Performs drug analysis as described in Figure 5.

### 7. **Stage_Analysis.ipynb**
   - **Purpose**: Conducts co-association analysis between cancer hallmarks and AJCC/TNM staging, as visualized in Figure 3.

## Usage
Each file is self-contained and should be executed in the specified order to reproduce results and analyses as per the OncoMark project. Refer to the accompanying documentation or comments within each file for additional guidance.
