# ATMcontroller_BearRobotics
This project is a simple ATM controller.
This controller has following functions.
1. See Balance
1. Deposit
1. Withdraw

## Project Structure
In root:
`bankAPI` is a sample bank API.
`main` is the file where this program runs.

`classes` contains classes used in this project.
Within `classes`:
`Account` is about Bank account.
`State` is an enum class about states of this program.
`User` is about User.

## Getting Started
1. Clone this repository.
`git clone https://github.com/GrapeDiget/ATMcontroller_BearRobotics.git`
1. run `main.py`.
`python main.py`

## Guide
<center>
  <img
    src="/images/activity%20diagram.png"
    height="300"
  />
</center>

* * *
At first, the state is `INIT`.
<center>
  <img
    src="/images/init.png"
  />
</center>

You can insert Card.
* * *
If you choose `1`, enter your Card number and PIN number.
<center>
  <img
    src="/images/insertCard.png"
  />
</center>

This program can enter any card number.
PIN number is any 4 length number.
* * *
And then, the state will be `MAIN`.
<center>
  <img
    src="/images/main.png"
  />
</center>

You can select account.
Basically, two account will appear.
Account number is random 10 length number.
* * *
If you choose option, the state will be `ACCOUNT`.
<center>
  <img
    src="/images/account.png"
  />
</center>

1. See Balance
<center>
  <img
    src="/images/see balance.png"
  />
</center>

* Show current balace.

2. Deposit
<center>
  <img
    src="/images/deposit.png"
  />
</center>

* When you enter the amount, the balance increases by the amount

3. Withdraw
<center>
  <img
    src="/images/withdraw.png"
  />
</center>

* When you enter the amount, the balance decreases by the amount.
If the balance is insufficient, the action will be cancle.

4. Select another account
* The state will switch to `ACCOUNT`