import csv
import os
print("Current working directory")
print(os.getcwd())
print("\n Students who passed:")
with open("D:\Internship\AIML-INTERNSHIP\day7\student.csv","r")as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["Status"]=="Pass":
            print(row["Name"])