import csv
import warnings
from decimal import Decimal

def load(path):
    rows = list(csv.DictReader(open(path)))
    return rows

def total_due(rows):
    total = Decimal("0")
    for r in rows:
        if not r["amount"].strip():
            warnings.warn("Skipping row with blank amount")
            continue
        if r["status"].lower() == "unpaid":
            total += Decimal(r["amount"])
    return total

if __name__ == "__main__":
    print(total_due(load("invoices.csv")))
