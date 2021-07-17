from openpyxl import load_workbook

wb = load_workbook(filename='ap_data.xlsx').worksheets[0]
print(wb)
count = 0
for row in wb:
    fields = []
    count += 1
    for i in range(0,8):
        fields.append(row[i].value)
    try:
        float(fields[1])
        float(fields[2])
    except:
        print(count)
        continue
    if fields[1] or fields[2]:
        continue
    else:
        print(count)    