---
config:
  theme: neo
  look: neo
  layout: elk
---
flowchart TD
 subgraph subGraph0["Data Preparation"]
        B1["Data Preprocessing"]
        C["Data Quality Control"]
        D["Hallmark-Specific Gene Scoring"]
  end
 subgraph subGraph1["Web-based tool"]
        B2["Web-server"]
  end
 subgraph subGraph2["Gene Set Details"]
        D1a["Curated Gene Sets from Databases"]
        D1b["Filtered Genes with High Hazard Ratios"]
        D1c["Manual Review for Biological Relevance"]
  end
 subgraph subGraph3["Hallmark Scoring Process"]
        D1["Gene Set Curation"]
        subGraph2
        D2["UCell Scoring Algorithm"]
        D3["Compute Digital Scores for Hallmarks"]
  end
 subgraph subGraph4["Thresholding and Annotation"]
        E["Binary Annotation Using Otsu Thresholding"]
        E1["Set Tissue-Specific Thresholds"]
        E2["Classify Cells: Positive or Negative"]
  end
 subgraph subGraph5["Synthetic Data Creation Details"]
        F1["Select 200 Cells per Patient per Hallmark"]
        F2["Group by Positive and Negative Status"]
        F3["Aggregate to Mimic Biopsy Samples"]
        F4["Create Balanced Datasets"]
  end
 subgraph subGraph6["Synthetic Dataset Creation"]
        F["Synthetic Bulk Dataset Creation"]
        subGraph5
        G["Processed Data Ready for Training"]
  end
 subgraph subGraph7["Model Architecture"]
        H1["Shared Base Layer"]
        H2["Task-Specific Layers"]
        H3["Output Layers with Sigmoid Activation"]
  end
 subgraph subGraph8["Neural Network Model"]
        H["Multi-Task Neural Network"]
        subGraph7
  end
 subgraph subGraph9["Training Details"]
        I1["Binary Cross-Entropy Loss"]
        I["Training Configuration"]
        I2["Adam Optimizer with Learning Rate"]
        I3["Learning Rate Scheduler: Halve on No Improvement"]
        I4["Early Stopping with Patience of 6 Epochs"]
  end
 subgraph subGraph10["Training Process"]
        J1["50 Epochs with Batch Size of 256"]
        J["Model Training"]
        J2["Forward Pass: Compute Predictions"]
        J3["Backward Pass: Compute Gradients"]
        J4["Parameter Updates: Optimize Weights"]
  end
 subgraph subGraph11["Model Training and Validation"]
        subGraph9
        subGraph10
        K["Validation Loss Monitoring"]
  end
 subgraph Metrics["Metrics"]
        M1["Accuracy"]
        M2["Precision"]
        M3["Recall"]
        M4["F1-Score"]
        M5["AUROC and AUPRC"]
  end
 subgraph subGraph13["Testing and Evaluation"]
        L["Internal Testing: 5-Fold Cross-Validation"]
        M["Performance Metrics"]
        Metrics
  end
 subgraph subGraph14["Predictive Outcomes"]
        P["Predict Hallmark Activities"]
        Q["Generate Detailed Report"]
        R["Heatmaps, Probability Distributions, Clinical Insights"]
  end
 subgraph Outputs["Outputs"]
        S["Sample specific analysis for personalized diagnosis and treatment"]
        T["Research Insights for Oncologists"]
  end
 subgraph Deployment["Deployment"]
        U1["Sample specific analysis"]
        U2["Prediction of hallmarks of cancer"]
        U3["Upload input dataset"]
        U4["Web Server for User Interaction"]
  end
    A["Clinician/Researcher"] -- Upload single-cell Transcriptomics Data --> B1
    A["Clinician/Researcher"] -- Upload Transcriptomics Data --> B2
    B1 --> C
    C --> D
    B2 --> U4
    D --> D1
    D1 --> D2
    D2 --> D3
    D3 --> E
    E --> E1
    E1 --> E2
    E2 --> F
    F --> G
    G --> H
    H --> H1 & I & P
    H1 --> H2
    H2 --> H3
    I --> I1 & I2 & I3 & I4 & J
    J --> J1 & K & L
    J1 --> J2 & J3 & J4
    L --> M
    M -- Logged --> K
    K --> N["External Validation on Independent Datasets"]
    N --> O["Performance Verification with Real-World Data"]
    P --> Q
    Q --> R
    R --> S & T
    U4 --> U3
    U3 --> U2
    U2 --> U1
    G@{ shape: db}
    style subGraph5 fill:#FFF9C4
    style G stroke:#AA00FF,color:#000000,fill:#00C853
    style subGraph7 fill:#E1BEE7
    style subGraph9 fill:#E1BEE7
    style subGraph10 fill:#E1BEE7
    style Metrics fill:#FFF9C4
    style A fill:#00C853,color:#000000
    style subGraph13 fill:#FFCDD2
    style subGraph3 fill:#FFCDD2
    style subGraph6 fill:#FFCDD2
    style subGraph8 fill:#FFE0B2
    style subGraph11 fill:#FFE0B2
    style subGraph0 fill:#FFCDD2
    style Deployment fill:#FFE0B2
    style subGraph4 fill:#FFCDD2
    style subGraph14 fill:#FFE0B2
    style Outputs fill:#FFCDD2
    style subGraph1 fill:#FFE0B2
    linkStyle 0 stroke:#000000,fill:none
