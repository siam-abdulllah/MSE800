from database import create_table
from user_manager import BankingManager

def main():
    create_table()
    manager = BankingManager()
    
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Register New Customer")
        print("2. Create New Account")
        print("3. Add Currency Type")
        print("4. Set Exchange Rate")
        print("5. Make a Transaction (Deposit/Withdraw)")
        print("6. View Transaction History")
        print("7. View All Customers")
        print("8. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            fname = input("First Name: ")
            lname = input("Last Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_customer(fname, lname, phone, email)
            
        elif choice == '2':
            c_id = int(input("Customer ID: "))
            name = input("Account Name: ")
            a_type = input("Type: ")
            bal = float(input("Initial Deposit: "))
            manager.create_account(name, a_type, bal, c_id)

        elif choice == '3':
            name = input("Currency Name (e.g., Dollar): ")
            symbol = input("Symbol (e.g., $): ")
            country = input("Country: ")
            manager.add_currency(name, symbol, country)

        elif choice == '4':
            curr_id = int(input("Currency ID: "))
            rate = float(input("Current Rate: "))
            manager.set_exchange_rate(curr_id, rate)

        elif choice == '5':
            acc_id = int(input("Account ID: "))
            amt = float(input("Amount (use negative for withdrawal): "))
            curr_id = int(input("Currency ID: "))
            manager.record_transaction(acc_id, amt, curr_id)

        elif choice == '6':
            acc_id = int(input("Enter Account ID: "))
            logs = manager.view_transactions(acc_id)
            for l in logs:
                print(f"ID: {l[0]} | Amt: {l[1]} {l[3]} | Date: {l[2]}")
            
        elif choice == '7':
            customers = manager.view_customers()
            for c in customers:
                print(f"{c[0]} | {c[1]} {c[2]} | {c[4]}")
                
        elif choice == '8':
            break

if __name__ == "__main__":
    main()