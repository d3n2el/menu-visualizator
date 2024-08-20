from tabulate import tabulate
import csv
import sys
import os
def main():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)< 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        with open(f"{sys.argv[1]}") as csvfile:
            menureader = csv.DictReader(csvfile)
            menu = [row for row in menureader]
            print(tabulate(menu, headers="keys", tablefmt="grid"))






main()




