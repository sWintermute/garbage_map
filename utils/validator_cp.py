from openpyxl import load_workbook

wb = load_workbook(filename='cp_data.xlsx').worksheets[0]
print(wb)
count = 0
for row in wb:
    fields = []
    count += 1
    for i in range(0,6):
        fields.append(row[i].value)
    try:
        float(fields[4])
        float(fields[5])
    except:
        print(count, fields[4], fields[5])
        continue
    if fields[2] and fields[3] and fields[0] :
        continue
    else:
        print(count)    