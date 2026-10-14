import csv

def load(path):
    rows = list(csv.DictReader(open(path)))
    return rows

def total_due(rows):
    total = 0
    for r in rows:
        if r["status"] == "unpaid":
            total += int(r["amount"])
    return total

if __name__ == "__main__":
    print(total_due(load("invoices.csv")))
