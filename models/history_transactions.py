class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def format_statement(self) -> list:
        """Transforma os objetos de transação em linhas de texto formatadas."""
        results = []
        for t in self._transactions:
            t_type = t.__class__.__name__
            symbol = "(+)" if t_type == "Deposit" else "(-)"
            results.append(f"{t_type}:\tR$ {t.amount:.2f} {symbol}")
        return results