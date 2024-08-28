import pandas as pd
from GSVA import gsva, gmt_to_dataframe
from plotnine import *
from sklearn.manifold import TSNE



# 读取基因集文件
genesets_df = gmt_to_dataframe('data/c2.cp.v2024.1.Hs.symbols.gmt')

# 读取基因表达文件
expression_df = pd.read_csv('data/GeneExpression.2024-08-20.tsv', sep='\t')
expression_df.set_index(expression_df.columns[0], inplace=True)
expression_df = expression_df.T

# GSVA
pathways_df = gsva(expression_df, genesets_df)

# 结果
print(pathways_df.head())
