from .Account import Account
from typing import Dict, List
import random
import string


class User:
    def __init__(self) -> None:
        self.__accountList: Dict[str, Account] = dict()
        self.__createAccount()
        self.__createAccount()

    def __createAccount(self) -> None:
        newAccountNumber = ''.join(random.sample(string.digits, 10))
        newAccount = Account(newAccountNumber)
        self.__accountList[newAccountNumber] = newAccount

    def getAccountList(self) -> List[str]:
        return list(self.__accountList.keys())

    def getAccount(self, accountNum: str) -> Account:
        return self.__accountList[accountNum]
