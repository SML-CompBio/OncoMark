## Single-Cell Support

The **OncoMark** tool is specifically designed for **bulk transcriptomics** data and is **not directly applicable** to raw single-cell RNA-seq (scRNA-seq) datasets, since **Hallmark gene sets** represent coordinated biological programs best captured at the population level.

However, if you are working with **single-cell transcriptomic data from patient samples**, there are several strategies to adapt OncoMark or Hallmark analysis for meaningful interpretation:

---

### 1. Pseudo-Bulk Aggregation (Per Patient)

If your goal is to assess Hallmark activity **per patient**, you should:

- **Aggregate gene expression** by summing the expression values of each gene across all cells within each patient sample.
- This creates a **pseudo-bulk profile** that mimics a bulk transcriptome.
- You can then apply **OncoMark** to these pseudo-bulk profiles to estimate **Hallmark pathway activity** at the patient level.

---

### 2. Cluster-Level Analysis (Within Sample)

If your goal is to analyze **specific groups or clusters of cells** (e.g., T cells, macrophages, tumor subtypes) within a sample:

- Perform clustering or cell type or state annotation.
- **Aggregate gene expression** by summing the expression values of each gene across all cells within each cluster.
- Apply **OncoMark** to the aggregated profile of each cluster to estimate Hallmark pathway activity for that specific **cell group or population**.

---

### 3. Single-Cell Level Scoring (Digital Scores)

If you need to assign **Hallmark activity scores to individual cells**, use a method designed for single-cell data, such as:

- **UCell**: A rank-based scoring method robust to scRNA-seq sparsity and dropout.
- Use the curated **Hallmark gene sets** provided in the `data/` directory of the GitHub repository.
- Scripts for computing UCell scores using both **Python** and **R** are available in the `src/` directory of the same repository.

This approach enables you to evaluate Hallmark signature activity **at single-cell resolution**, suitable for downstream tasks.

---

### Summary

| Use Case                        | Method                          | Tool      |
|---------------------------------|----------------------------------|-----------|
| Per-patient Hallmark activity   | Aggregate all cells → Pseudo-bulk | OncoMark  |
| Per-cluster Hallmark activity   | Aggregate cells in a cluster      | OncoMark  |
| Per-cell Hallmark scoring       | Use UCell with Hallmark gene sets | UCell     |