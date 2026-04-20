# Arquivo: models/account.py

from models.history_transactions import History

class Account:
    def __init__(self, number: int, client):
        self._balance = 0.0
        self._number = number
        self._branch = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, number: int):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def branch(self):
        return self._branch

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, amount: float) -> tuple[bool, str]:
        if amount > self._balance:
            return False, "Insufficient funds."
        
        if amount > 0:
            self._balance -= amount
            return True, "Withdrawal successful!"
        
        return False, "Invalid withdrawal amount."

    def deposit(self, amount: float) -> tuple[bool, str]:
        if amount > 0:
            self._balance += amount
            return True, "Deposit successful!"
        
        return False, "Invalid deposit amount."


class CheckingAccount(Account):
    def __init__(self, number: int, client, limit=500.0, withdrawal_limit=3):
        # Aqui ele chama o __init__ da classe Account ali de cima!
        super().__init__(number, client)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit

    def withdraw(self, amount: float) -> tuple[bool, str]:
        number_withdrawals = len(
            [t for t in self.history.transactions if t.__class__.__name__ == "Withdrawal"]
        )

        exceeded_limit = amount > self._limit
        exceeded_withdrawals = number_withdrawals >= self._withdrawal_limit

        if exceeded_limit:
            return False, "Withdrawal amount exceeds the limit."
        elif exceeded_withdrawals:
            return False, "Maximum number of withdrawals exceeded."
        else:
            return super().withdraw(amount)