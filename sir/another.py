import openpyxl as oxl
a="/home/anu/Downloads/work/niitluck/sir/Financial Sample.xlsx"
xlsx_wb=oxl.load_workbook(filename=a)
sheets=xlsx_wb.get_sheet_names()
xlsx_ws=xlsx_wb[sheets[0]]
labels=[cell for cell in xlsx_ws]
data=[]
#for row in xlsx_ws.rows[1:]:
 #   data.append(cell.value for cell in row)
#print([item[labels.index('Product')]]for item in data[0,10])
