import pandas as pd 
a="Financial Sample.xlsx"
b="sample.xlsx"
xlsx_file=pd.ExcelFile(a)
xlsx_read={sheetname:xlsx_file.parse(sheetname) for sheetname in xlsx_file.sheet_names}
print(xlsx_read['Sheet1'].head(10)['Segment'],end=" ")
print(xlsx_read['Sheet1'].head(10)['Product'])
xlsx_read['Sheet1'].to_excel(b,'Sheet1',index=False)
