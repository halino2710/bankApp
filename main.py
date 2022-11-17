print("Welcome to Ing Hamed Idriss Kemokai's International Bank")
print("Please follow the on-screen instructions\n")

balance = float(100)

global user_pin

while True:
    user_pin = 1234
    pin_entered = int(input("Enter your pin: "))
    if user_pin != pin_entered:
        print("Invalid pin, please try again!")
        continue
    else:
        break


def main():

    print("""
            Enter
    1: ----> to check your balance
    2: ----> to withdraw fund
    3: ----> to deposit
    4: ----> to change password
    5: ----> to quit
    """)
    user_input = input()

    while user_input != "q":
        if user_input == '1':
            check_balance()
        elif user_input == '2':
            withdraw()
        elif user_input == '3':
            deposit()
        elif user_input == '4':
            change_password()
        elif user_input == '5':
            print("Thank you for using the service!")
            break
        else:
            print("Invalid command entered, please try again!")

        print("""
                    Enter
            1: ----> to check your balance
            2: ----> to withdraw fund
            3: ----> to deposit
            4: ----> to change password
            5: ----> to quit
            """)
        user_input = input()
        print()


def check_balance():
    print(f"\nYour account balance is {balance} SLL\n")


def withdraw():
    global balance
    withdraw_amount = float(input("Amount you wish to withdraw: "))
    if withdraw_amount > balance:
        print("You have insufficient fund.")
    else:
        print(f"You have successfully withdrawn {withdraw_amount} SLL\n")
        new_balance = balance - withdraw_amount
        print(f"Your new account balance is {new_balance} SLL")
        balance = new_balance


def deposit():
    global balance
    deposit_amount = float(input("Deposit amount: "))
    print(f"You have deposited to your account: {deposit_amount}")
    balance = balance + deposit_amount
    print(f"Your new account balance is: {balance}")


def change_password():
    while pin_entered != 'q':
        global user_pin
        old_pin = int(input("Enter you old pin: "))
        if old_pin == user_pin:
            new_pin = int(input("Enter new pin: "))
            confirm_new_pin = int(input("Confirm new pin: "))
            while old_pin != 'q':
                if new_pin == confirm_new_pin:
                    print("You have successfully changed your pin")
                    print(f"Your new pin is: {new_pin}")
                    user_pin = new_pin
                    print(user_pin)
                    return
                else:
                    print("Pin does not match")
                    break
        else:
            print("Pin entered does not match current pin.")


main()
