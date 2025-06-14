import csv

with open('grades.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    data = [(row[0], int(row[1])) for row in reader]

data.sort(key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(data, start=1):
    print(f"{rank}. {name} - {score}分")