import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# -------------------- DATA HANDLING --------------------

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note (optional): ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!")


def read_expenses():
    expenses = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses


# -------------------- DISPLAY --------------------

def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for e in expenses:
        print(f"{e['Date']} | {e['Category']} | ₹{e['Amount']} | {e['Note']}")


def show_dashboard():
    expenses = read_expenses()
    if not expenses:
        print("No data to show dashboard.")
        return

    category_totals = {}

    for e in expenses:
        category = e["Category"]
        category_totals[category] = category_totals.get(category, 0) + e["Amount"]

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution by Category")
    plt.show()


# -------------------- MAIN MENU --------------------

def main():
    initialize_file()

    while True:
        print("\n💰 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Dashboard")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_dashboard()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
