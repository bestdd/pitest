import os

import pandas as pd
from pandas import DataFrame


def read_excel(path, sheel_name):
    df = pd.read_excel(path, sheel_name)
    df1 = df.values.tolist()
    return df.values.tolist()


def update_excel(path, sheel_name, row_num, col_name, value ):
    df = pd.read_excel(path, sheel_name)
    df.loc[row_num, col_name] = value
    DataFrame(df).to_excel(path, sheel_name, index=False, header=True)


if __name__ == '__main__':
    xlsx_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    df = read_excel(xlsx_path + '/resource/case-template.xlsx', '工作表1')
    update_excel(xlsx_path + '/resource/case-template.xlsx', '工作表1', 1, "执行结果", "on")





