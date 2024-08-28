import pandas as pd

# Handle the gene expression data
expression_df_raw = pd.read_csv('../data/GDSC/Cell_line_RMA_proc_basalExp.txt', sep='\t') # Read the file

expression_df = expression_df_raw.drop(expression_df_raw.columns[1], axis=1) # Drop the first column
expression_df.set_index(expression_df.columns[0], inplace=True) # Set the first column as the index
expression_df = expression_df[expression_df.index.notnull()] # Remove any null values

# TODO(zhong): Add more data processing steps here
expression_df.head(10000).to_csv('expression_df.csv', index=True) # Save the first 10000 rows to a new file