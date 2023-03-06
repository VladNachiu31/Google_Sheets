import gspread

# in secrets.json you must include the api's keys from Google Drive and spreadsheet

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('name_of_spreadsheet')

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name
worksheet1 = spreadsheet.worksheet('name_of_sheet')

# Get a row or rows by cells
rows = worksheet1.get_values('A5:F7')

# Get a row by index
rows = worksheet1.row_values(3)

# Get a column by index
column = worksheet1.col_values(2)[1:]

print(rows)
