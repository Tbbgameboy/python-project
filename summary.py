import csv 
from prettytable import from_csv

def show_summary():
    print('This is the summary of our expense tracker developed by saintdave. Thank you for using our website.')

    sum = 0
    count = 0
    with open("expense_tracker.csv", newline="\n") as f:
        mytable = from_csv(f)

        print(mytable)


    with open("expense_tracker.csv", newline="") as f:
        reader = csv.DictReader(f) 
        for row in reader:
            sum += float(row["amount"]) 
            count +=1 

        print("Total Amount:", sum)
        print("Total Expenses", count)
        
        
