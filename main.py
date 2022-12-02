import bankAPI
from classes.Account import Account
from classes.State import State
from classes.User import User

state: State = State.INIT
selectedAccount: Account = Account('')


def insertCard() -> bool:
    global state, user
    print("Enter your Card number")
    cardNum = input()
    print("Enter your PIN number")
    pin = input()
    if bankAPI.enterPIN(cardNum, pin):
        state = State.MAIN
        user = User()
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        if state == State.INIT:
            print("Welcome to ATM controller!")
            print("Please choose an action.")
            while True:
                print("1: Insert Card")
                print("0: exit")
                action = input()
                if not action.isdigit():
                    print("\nWrong action! Please choose again.")
                    continue
                action = int(action)
                if action == '0':
                    print("Good Bye!")
                    exit()
                elif action != 1:
                    print("\nWrong action! Please choose again.")
                    continue

                result = insertCard()
                if result:
                    break
                else:
                    print("\nWrong action! Check your card again.")
                    continue

        elif state == State.MAIN:
            print("========================")
            print("Select the account number you want to check")
            accountList = user.getAccountList()
            while True:
                for i in range(len(accountList)):
                    print(f'{i+1}: {accountList[i]}')
                print("0: exit")
                action = input()
                if not action.isdigit():
                    print("\nWrong action! Please select again.")
                    continue
                action = int(action)
                if action > len(accountList):
                    print("\nWrong action! Please select again.")
                    continue
                elif action == 0:
                    print("Good Bye!")
                    exit()

                selectedAccount = user.getAccount(accountList[action-1])
                state = State.ACCOUNT
                break

        elif state == State.ACCOUNT:
            print("========================")
            print("Selected account number is " + selectedAccount.getAccountNum())
            print("Please choose an action.")
            while True:
                print("1: See Balance")
                print("2: Deposit")
                print("3: Withdraw")
                print("4: Select another account")
                print("0: exit")
                action = input()
                if not action.isdigit():
                    print("\nWrong action! Please choose again.")
                    continue
                action = int(action)
                if action == 1:
                    state = State.BALANCE
                elif action == 2:
                    state = State.DEPOSIT
                elif action == 3:
                    state = State.WITHDRAW
                elif action == 4:
                    state = State.MAIN
                elif action == 0:
                    print("Good Bye!")
                    exit()
                else:
                    print("\nWrong action! Please choose again.")
                    continue
                break

        elif state == State.BALANCE:
            print("========================")
            print("This is your current balance")
            print(f"${selectedAccount.getBalance()}")
            state = State.ACCOUNT
        
        elif state == State.DEPOSIT:
            print("========================")
            print("Enter the amount to deposit")
            amount = int(input())
            if selectedAccount.deposit(amount):
                print("Deposit success!")
            print("This is your current balance")
            print(f"${selectedAccount.getBalance()}")
            state = State.ACCOUNT
        
        elif state == State.WITHDRAW:
            print("========================")
            print("Enter the amount to withdraw")
            amount = int(input())
            if selectedAccount.withdraw(amount):
                print("Withdraw success!")
            else:
                print("Withdraw falied due to insufficient balance")
            print("This is your current balance")
            print(f"${selectedAccount.getBalance()}")
            state = State.ACCOUNT