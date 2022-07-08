import xlsxwriter

workbook = xlsxwriter.Workbook('Example3.xlsx')
worksheet = workbook.add_worksheet("My sheet")
bold = workbook.add_format({'bold': 1})

scores = (
    ['CN143', "PASS"],
    ['JP167', "PASS"],
    ['JP128', "PASS"],
    ['CN456', "PASS"],
)

row = 0
col = 0

for name, score in (scores):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score, bold)
    row += 1

workbook.close()
