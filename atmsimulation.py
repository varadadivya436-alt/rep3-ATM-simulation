balance = 1000
pin = "1234"

user_pin = input("Enter PIN: ")

if user_pin == pin:
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance = balance + amount
        print("New Balance =", balance)

    elif choice == "3":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Choice")

else:
    print("Wrong PIN")