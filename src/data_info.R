library(dplyr)
library(Seurat)
library(Matrix)
library(sva)
library(ggplot2)
library(harmony)

read_data <- function(folder_path) {
  cells <- read.csv(file.path(folder_path, "Cells.csv"), row.names = 1)
  genes <- read.table(file.path(folder_path, "Genes.txt"), header = FALSE)
  mtx_files <- list.files(folder_path, pattern = "\\.mtx$", full.names = TRUE)
  if (length(mtx_files) == 0) {
    stop("No .mtx file found in the folder: ", folder_path)
  }
  exp_data_df <- readMM(mtx_files[1])
  rownames(exp_data_df) <- make.unique(toupper(genes$V1), sep = "_")
  colnames(exp_data_df) <- rownames(cells)
  exp_data_df <- exp_data_df[!duplicated(rownames(exp_data_df)), ]
  exp_data_df <- CreateSeuratObject(counts = exp_data_df, min.cells = 3, min.features = 200)
  exp_data_df[["percent.mt"]] <- PercentageFeatureSet(exp_data_df, pattern = "^MT-")
  write.csv(exp_data_df@meta.data, file = file.path(folder_path, "data_info.csv"))
  rm(exp_data_df)
  gc()
}

folders <- list.dirs("outlier_scrnaseq", recursive = FALSE)
for (folder in folders) {
  read_data(folder)
}
