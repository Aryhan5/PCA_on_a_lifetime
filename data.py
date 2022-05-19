'''
Lecture - écriture, pré et post-processing de données
'''

import pandas as pd
import gtsam as gtsm

def generate_tag_stickers_data(data, path):
    new_col = data["ID"].astype(str)
    new_col = new_col.str.pad(width=3, side='left', fillchar='0')
    rt = data[["ID", "Description"]]
    rt["Path"] = path + new_col + ".png"
    return rt

def import_from_datasheet(sheet_path):
    #Error in sheet format must be checked here
    df = pd.read_excel(sheet_path)
    df.set_index("ID")
    return df

def agregate(meta_data, apriltag_data):
    print()

def remap(observed_data, sheet_data):
    print()

def export(new_data, sheet_path, create=False):
    if create:
        open(sheet_path, "x")
    xls = pd.read_excel(sheet_path)
    xls.set_index('ID')    
    df = pd.merge(xls, new_data, on="ID", how="outer")
    df.to_excel("Mapped_"+sheet_path)


