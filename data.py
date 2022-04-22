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
    print()

hb = import_from_datasheet("./Habitudes.xlsx")


