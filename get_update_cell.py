import gspread
import re
import statistics

# in secrets.json you must include the api's keys from Google Drive and spreadsheet

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('name_of_spreadsheet')

# Get worksheet
worksheet1 = spreadsheet.worksheet('name_of_sheet')

# Get cell
cell1 = worksheet1.get_values('D5')[0][0]

# Get cell using acell
cell2 = worksheet1.acell('D5').value

# Search for a cell
cell3 = worksheet1.find('-10')

# Search for many cells
cells = worksheet1.findall('-9')

# Search for partial matches
reg = re.compile(r'99')
cells = worksheet1.findall(reg)

for cell in cells:
  print(cell.row, cell.col)


# Update a cell
worksheet1.update('E5', -29)

# Update a cell based on row-column
worksheet1.update_cell(5, 5, -39)


# update Celsius to Fahrenheit and change the name of the column

existing_column = worksheet1.get_values('E2:E25')
new_column = [[round((float(i[0]) * 9/5 + 32), 1)] for i in existing_column]


worksheet1.update('G1:G25', [['Fahrenheit']] + new_column)

# Get existing columns
existing_column = worksheet1.get_values('E2:E25')

# Flatten the existing column
existing_column = [float(i[0]) for i in existing_column]

# Calculate average and add the Worksheet
average = statistics.mean(existing_column)
worksheet1.update('last_row', average)