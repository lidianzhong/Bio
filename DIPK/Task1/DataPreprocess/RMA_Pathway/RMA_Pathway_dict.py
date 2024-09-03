import pandas as pd
import joblib

dataset = pd.read_csv('../../Dataset/pathway.csv', header=0)

RMA_Pathway_dict = {'.'.join(str(Cell).split('.')[1:]): dataset[Cell].tolist() for Cell in dataset.columns[1:]}

joblib.dump(RMA_Pathway_dict, 'RMA_Pathway_dict.pkl')