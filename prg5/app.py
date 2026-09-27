import csv

student = []
with open("student.csv", "r") as f: 
    reader = csv.DictReader(f) 
    for row in reader:
        student.append((row["Name"], int(row["Marks"])))

maxmarks = max(mark for name, mark in student) 

for name, mark in student: 
    bar = "=" * (mark*50//maxmarks) 
    print(name, "|", bar, mark)