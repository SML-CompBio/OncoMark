library(Matrix)
library("UCell")
set.seed(123)

gene <- read.csv2('hallmark_surv_curated.csv', sep=',')

geneSets <- list()
for (col_name in names(gene)) {
  geneSets[[col_name]] <- gene[[col_name]][!is.na(gene[[col_name]]) & gene[[col_name]] != ""]
}


calculate_and_save_scores <- function(folder_path) {

  # Read files
  cells <- read.csv(file.path(folder_path, "Cells.csv"), row.names = 1)
  genes <- read.table(file.path(folder_path, "Genes.txt"), header = FALSE)
  mtx_files <- list.files(folder_path, pattern = "\\.mtx$", full.names = TRUE)
  if (length(mtx_files) == 0) {
    stop("No .mtx file found in the folder: ", folder_path)
  }
  
  # Convert to dataframe
  exp_data_df <- readMM(mtx_files[1])
  exp_data_df <- as(exp_data_df, "CsparseMatrix")
  rownames(exp_data_df) <- genes
  colnames(exp_data_df) <- rownames(cells)
  
  # Calculate scores
  u.scores1 <- ScoreSignatures_UCell(exp_data_df, features = geneSets, ncores = 10)
  # Save scores as CSV
  write.csv(u.scores1, file = file.path(folder_path, "score_hallmark_surv.csv"))

  rm(exp_data_df)
  gc()
}

folders <- list.dirs("outlier_scrnaseq", recursive = FALSE)
for (folder in folders) {
  calculate_and_save_scores(folder)
}
