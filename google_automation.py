import xlrd
from xlwt import Workbook
from googlesearch import search
  
loc = ("/home/Bhagath/Account.xlsx") 

wb_save = Workbook()
sheet1 = wb_save.add_sheet('Sheet 1', cell_overwrite_ok=True) 
sheet1.write(0, 0, 'SL NO') 
sheet1.write(0, 1, 'COMPANY NAME') 
sheet1.write(0, 2, 'GOOGLE URL') 
sheet1.write(0, 3, 'LINKEDIN') 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

value = 1
#ncols for col,sheet.nrows  
for i in range(1, sheet.nrows):
    sheet1.write(i, 0, sheet.cell_value(i, 0)) 
    sheet1.write(i, 1, sheet.cell_value(i, 1)) 
    sheet1.write(i, 2, sheet.cell_value(i, 2))  
    company_name = sheet.cell_value(i, 1)
    query = res = "".join((company_name, " CFO :linkedin"))
    try: 
        for linkedin_url in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
            sheet1.write(i, 3, linkedin_url)
            print linkedin_url
            print i
    except:
        sheet1.write(i, 3, "TIMEOUT")
        print("some error")
wb_save.save('test.xls')

