#!/usr/bin/env Rscript

library(GSEABase)
library(GSVA)

# gene expression file
file_path <- "expression_df.csv"
X <- as.matrix(read.csv(file_path, header = TRUE, row.names = 1))

# gene set file
gmt_file <- "../data/Msigdb/c2.cp.v2024.1.Hs.symbols.gmt"
gene_sets <- getGmt(gmt_file)

gs <- lapply(gene_sets, geneIds)
names(gs) <- names(gene_sets)

# create GSVA parameter object
gsvaPar <- gsvaParam(X, gs)

# print GSVA parameter object
print(gsvaPar)

# run GSVA
gsva.es <- gsva(gsvaPar, verbose = FALSE)

# save GSVA results
write.csv(gsva.es, "pathway.csv")
