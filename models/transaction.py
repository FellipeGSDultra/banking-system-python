from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def register(self, account) -> tuple[bool, str]:
        pass

class Withdrawal(Transaction):
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account) -> tuple[bool, str]:
        sucesso, mensagem = account.withdraw(self.amount)
        if sucesso:
            account.history.add_transaction(self)
        return sucesso, mensagem

class Deposit(Transaction):
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account) -> tuple[bool, str]:
        sucesso, mensagem = account.deposit(self.amount)
        if sucesso:
            account.history.add_transaction(self)
        return sucesso, mensagem