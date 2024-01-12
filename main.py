from openpyxl import load_workbook


wb = load_workbook(filename="questions\\questions.xlsx")

sheet_ranges = wb["Лист1"]
QUESTIONS = []
ANSWER = []


for n, q, a in sheet_ranges:
    if q.value and n.value and n != "№":
        QUESTIONS.append(q.value)
        ANSWER.append(a.value)
print(QUESTIONS, ANSWER)
