class Account:

    def __init__(self):
        self._transactions = []
        self._transaction_len_when_entering_context = 0

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    def __enter__(self):
        self._transaction_len_when_entering_context = len(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.balance < 0:
            self._transactions = self._transactions[:self._transaction_len_when_entering_context]
