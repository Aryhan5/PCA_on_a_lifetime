'''
Lecture - écriture, pré et post-processing de données
'''

import numpy as np
import pandas as pd

def generate_tag_stickers_data(data, path):
    new_col = data["ID"].astype(str)
    new_col = new_col.str.pad(width=3, side='left', fillchar='0')
    rt = data[["ID", "Description"]]
    rt["Path"] = path + new_col + ".png"
    return rt



xls = pd.read_excel('../Habits_Clustering/Habitudes.xlsx')    
xls_data = generate_tag_stickers_data(xls, 'D:\\\\Work\\\\Ergonautique\\\\PCA_on_a_lifetime\\\\tags\\')
xls_data.to_excel("etiquettes.xlsx")