class ClientRepository:
    def __init__(self):
        self._clients = []

    def add_client(self, client):
        self._clients.append(client)

    def find_by_cpf(self, cpf: str):
        for client in self._clients:
            if client._cpf == cpf:
                return client
        return None

class AccountRepository:
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)
        
    def get_total_accounts(self) -> int:
        return len(self._accounts)