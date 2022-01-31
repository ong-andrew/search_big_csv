import csv
import sys

a = "search string"

b = csv.field_size_limit(sys.maxsize)

with open("file.csv") as f:
    reader = csv.reader(f, delimiter=':') #change the delimiter where appropriate.
    for line in reader:
        if a in line:
            print("FOUND! " + str(line))
            break
