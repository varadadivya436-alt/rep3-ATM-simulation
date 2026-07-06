# rep3-ATM-simulation
1.variable
balance=1000
pin="1234"
balance stores the money.
pin stores the ATMPIN
2.INPUT
user_pin=input("enter the pin")
the user enters the pin
3.PIN CHECKS
if user_pin==pin
if the pin is correct ,continue
otherwise print"wrong pin"
4.MENU
1.balance
2.despoite
3.withdraw
5.BALANCE
print(balance)
displays the current balance
6.DESPOITE
balance==balance+amount
adds the despoited money to the balance
7.WITHDRAW
balance=balance-amount
subtract the withdraw amount from the balance if enough money ios avalible
