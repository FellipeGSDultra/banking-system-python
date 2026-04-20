from models import account
from models.client import Individual
from models.account import CheckingAccount
from models.transaction import Deposit, Withdrawal
from models.input_validator import InputValidator
from models.repositories import ClientRepository, AccountRepository
from models.views import display_main_menu, display_statement

def main():
   
    client_repo = ClientRepository()
    account_repo = AccountRepository()

    while True:
        
        option = display_main_menu()

        if option == "d":
            
            print("\n--- Deposit Operation ---")
            cpf = InputValidator.get_string("Enter CPF: ")
            if not cpf: continue
            
            client = client_repo.find_by_cpf(cpf)

            if not client:
                print("\n[!] Client not found.")
                continue
                
            if not client._accounts:
                print("\n[!] This client has no accounts.")
                continue

            amount = InputValidator.get_float("Enter deposit amount: R$ ")
            if amount is None: continue

            transaction = Deposit(amount)
            account = client._accounts[0]
            
            success, message = client.perform_transaction(account, transaction)
            
            if success:               
                print(f"\n[OK] {message}")
            else:
                print(f"\n[ERROR] {message}")

        elif option == "w":
            
            print("\n--- Withdrawal Operation ---")
            cpf = InputValidator.get_string("Enter CPF: ")
            if not cpf: continue
            
            client = client_repo.find_by_cpf(cpf)

            if not client:
                
                print("\n[!] Client not found.")
                continue
                
            if not client._accounts:
                
                print("\n[!] This client has no accounts.")
                continue

            amount = InputValidator.get_float("Enter withdrawal amount: R$ ")
            if amount is None: continue

            transaction = Withdrawal(amount)
            account = client._accounts[0]
            
            success, message = client.perform_transaction(account, transaction)
            
            if success:
                
                print(f"\n[OK] {message}")

            else:
                
                print(f"\n[ERROR] {message}")

        elif option == "s":
            
            print("\n--- Bank Statement ---")
            cpf = InputValidator.get_string("Enter CPF: ")
            if not cpf: continue
            
            client = client_repo.find_by_cpf(cpf)

            if not client:
                
                print("\n[!] Client not found.")
                continue
                
            if not client._accounts:
                
                print("\n[!] This client has no accounts.")
                continue

            account = client._accounts[0]
            
            transaction_lines = account.history.format_statement()

            display_statement(account.balance, transaction_lines)
            

        elif option == "nu":
            
            print("\n--- New User ---")
            cpf = InputValidator.get_string("Enter CPF (numbers only): ")
            if not cpf: continue

            if client_repo.find_by_cpf(cpf):
                
                print("\n[!] A client with this CPF already exists!")
                continue

            name = InputValidator.get_string("Full name: ")
            birth_date = InputValidator.get_date("Birth date (dd-mm-yyyy): ")
            address = InputValidator.get_string("Full address: ")
            
            if name and birth_date and address:
                
                new_client = Individual(cpf=cpf, name=name, birth_date=birth_date, address=address)
                client_repo.add_client(new_client)
                print("\n[OK] Client successfully created!")

        elif option == "na":
            
            print("\n--- New Account ---")
            cpf = InputValidator.get_string("Enter client's CPF: ")
            if not cpf: continue 
            client = client_repo.find_by_cpf(cpf)

            if not client:
                print("\n[!] Client not found. Operation aborted.")
                continue

            account_number = account_repo.get_total_accounts() + 1
            new_account = CheckingAccount(number=account_number, client=client)
            
            account_repo.add_account(new_account)
            client.add_account(new_account)
            print(f"\n[OK] Account created! Branch: {new_account.branch} | Number: {new_account.number}")

        elif option == "q":
            
            print("\nExiting the system. Goodbye!")
            break
        
        else:
            print("\n[!] Invalid option.")


if __name__ == "__main__":
    main()