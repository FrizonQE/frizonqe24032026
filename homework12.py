import csv

with open("airport-codes_csv.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        if row["iso_country"] == "UA":
            print(row["name"])