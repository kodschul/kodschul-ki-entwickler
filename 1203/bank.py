from __future__ import annotations


class BankAccount:
    def __init__(self, accountNumber: str, ownerName: str, openingBalance: float = 0.0) -> None:
        if openingBalance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.balance = float(openingBalance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        return self.balance

    def transferTo(self, targetAccount: "BankAccount", amount: float) -> None:
        if targetAccount is self:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(amount)
        targetAccount.deposit(amount)

    def getSummary(self) -> str:
        return f"Account {self.accountNumber} | Owner: {self.ownerName} | Balance: ${self.balance:.2f}"


if __name__ == "__main__":
    mainAccount = BankAccount("DE-1001", "Alice", 500.0)
    savingsAccount = BankAccount("DE-2001", "Alice Savings", 150.0)

    mainAccount.deposit(200.0)
    mainAccount.withdraw(50.0)
    mainAccount.transferTo(savingsAccount, 100.0)

    print(mainAccount.getSummary())
    print(savingsAccount.getSummary())
