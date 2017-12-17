import json

import csv

infile = open("Paston_Letters_4.json","r")
outfile = open("Paston_Letters_gephi.csv","w")

writer = csv.writer(outfile)

data = json.loads(infile.read())

#writer.writerow(data[0].keys())  # header row

for row in data:
    writer.writerow(row.values())
