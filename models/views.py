def display_main_menu() -> str:
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    menu_text = """\n
    ================ BANK MENU ================
    [d]   Deposit
    [w]   Withdraw
    [s]   Statement
    [na]  New Account
    [nu]  New User
    [q]   Quit
    ===========================================
    Select an option:
    => """
    return input(menu_text).lower()


def display_statement(balance: float, transaction_lines: list):
    """Exibe o extrato formatado visualmente para o usuário."""
    print("\n================ STATEMENT ================")
    
    if not transaction_lines:
        print("No transactions found for this account.")
    else:
        for line in transaction_lines:
            print(line)
            
    print(f"\nCurrent Balance:\tR$ {balance:.2f}")
    print("==========================================")