from datetime import datetime

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.financial_manager = FinancialManager()
    
    def login(self, email, password):
        return self.email == email and self.password == password

class Transaction:
    def __init__(self, type, amount, description):
        self.type = type
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class FinancialManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, type, amount, description):
        transaction = Transaction(type, amount, description)
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions exist.")
            return
        counter = 1
        for t in self.transactions:
            print(f"{counter}. {t.date} - {t.type} - {t.amount} - {t.description}")
            counter += 1

    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            del self.transactions[index]
            print("Transaction deleted successfully.")
        else:
            print("Invalid transaction number.")

    def Final_report(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        savings = income - expenses
        print("**** Financial Report ****")
        print(f"Total Income: {income}")
        print(f"Total Expenses: {expenses}")
        print(f"Savings: {savings}")


def main():
    print("Welcome to Finance Manager")
    
    user = User("Amir", "a@b.com", "1111")
    
   
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        if user.login(email, password):
            print(f"You are logged in as {user.name}")
            break
        else:
            print("Invalid email or password. Please try again.")
    
   
    while True:
        print("**** Finance Manager ****")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Final Report")
        print("5. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            type = input("Transaction type (income/expense): ")
            amount = float(input("Amount: "))
            description = input("Description: ")
            user.financial_manager.add_transaction(type, amount, description)
        elif choice == "2":
            user.financial_manager.view_transactions()
        elif choice == "3":
            user.financial_manager.view_transactions()
            index = int(input("Enter the transaction number to delete: ")) - 1
            user.financial_manager.delete_transaction(index)
        elif choice == "4":
            user.financial_manager.Final_report()
        elif choice == "5":
            print(f"Thank you for using the application, {user.name}. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
