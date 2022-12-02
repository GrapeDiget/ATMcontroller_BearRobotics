class Account:
    def __init__(self, accountNumber) -> None:
        self.__accountNumber: str = accountNumber
        self.__balance: int = 0

    def getAccountNum(self) -> str:
        return self.__accountNumber

    def getBalance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> bool:
        self.__balance += amount
        return True

    def withdraw(self, amount: int) -> bool:
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False
