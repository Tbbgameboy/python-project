import csv


def run_add():
    name = input("Enter name: ")
    
    date = input("Enter date: ")

    amount = input("Enter amount: ")

    category = input("Enter category: ")

    with open("expense_tracker.csv", "a+", newline="\n") as f:
        writer = csv.DictWriter(f, ["name", "date", "amount", "category"])
        writer.writerow(
            {
                "name": name,
                "date": date,
                "amount": amount,
                "category": category,
            }
        )

    print("record successfully saved to your expense tracker.csv")
