from datetime import date

class Client:
    def __init__(self, address: str):
        self._address = address
        self._accounts = [] 

    def add_account(self, account):
        self._accounts.append(account)

    def perform_transaction(self, account, transaction) -> tuple[bool, str]:
        # Repassa o retorno (sucesso, mensagem) da transação
        return transaction.register(account)


class Individual(Client):
    def __init__(self, cpf: str, name: str, birth_date: date, address: str):
        super().__init__(address) 
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date