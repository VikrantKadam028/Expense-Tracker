def add_expense(expenses):
    date = input("Enter the date(YYYY-MM-DD) :")
    category = input("Enter the category :")
    description = input("Enter the description :")
    amount = float(input("Enter the amount :"))

    expense = {
        "date" : date,
        "category" : category,
        "description" : description,
        "amount" : amount
    }
    expenses.append(expense)
    print("Expense added successfully!!")


def view_expense(expenses):
    for expense in expenses:
        print(f"Date:{expense['date']}\nCategory:{expense['category']}\nDescription:{expense['description']}\nAmount:{expense['amount']}")


def delete_expense(expenses):
    description = input("Enter the description of expense to delete:")
    for expense in expenses:
        if expense['description'] == description:
            expenses.remove(expense)
            print("Expense Deleted.")
        else:
            print("Expense not found.")


def total_expence_category(expenses,category):
    total = 0
    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']
    print(f"The total expenses in category:\n{category} : {total}")
    

def total_expense_date(expenses,date):
    total = 0
    for expense in expenses:
        if expense['date'] == date:
            total += expense['amount']
    print(f"The total expenses in date:\n{date} : {total}")            


def main():
    expenses = []

    while True:
        print("********************")  
        print("Expense Tracking App")
        print("********************")  
        print("1.Add Expense\n2.View Expense\n3.Delete Expense\n4.Total Expense by category\n5.Total expense by date\n6.Exit")

        choice = int(input("Enter your choice :"))

        match choice:
            case 1:
                add_expense(expenses)
            case 2:
                view_expense(expenses)
            case 3:
                delete_expense(expenses)
            case 4:
                category = input("Enter the category :")
                total_expence_category(expenses,category)
            case 5:
                date = input("Enter the date (YYYY-MM-DD) :")
                total_expense_date(expenses,date)
            case 6:
                break
            case _:
                print("Invalid choice!!")

main()


        