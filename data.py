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


