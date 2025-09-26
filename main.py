from record import run_add
from summary import show_summary

while True:
    print(
"""  

Welcome to SaintDavy Expense Tracker\n
This app allow you to record, categorize and show the summary of your Financial Expenditure
Add record
Categorize your Record,
Show summary of your financial expenditure


1. Add Record
2. Show summary of your Financial expenditure
3. Quit

"""
    )

    option = input("Waiting for your response: ")

    if option == "1":
        run_add()
    elif option == "2":
        show_summary()
    else:
        print("Goodbye")
        break
