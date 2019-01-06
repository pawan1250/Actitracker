import pandas as pd

def get_sheet(file_path,sheetname):
    df=pd.read_excel(file_path,sheet_name=sheetname)
    return df

def get_rows(file_path,sheetname):
    df=get_sheet(file_path,sheetname)
    rows=df.shape[0]
    return rows

def get_data(file_path,sheetname,row_number,column_name):
    df=get_sheet(file_path,sheetname)
    value=df.loc[row_number,column_name]
    return value

def write_to_excel(file_path, sheetname, row_number,column_name,value_to_write):
    df=get_sheet(file_path,sheetname)
    df.loc[row_number,column_name]=value_to_write
    writer=pd.ExcelWriter(file_path)
    df.to_excel(writer,sheetname)
    writer.save()