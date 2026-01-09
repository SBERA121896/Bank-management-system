import  random
import os
import hashlib


def show_menu():
    print("\n🏦 Welcome to SBI Bank - Banking Management System")
    print('''
1. Create New Account  
2. Deposit Money  
3. Withdraw Money  
4. Transfer Money  
5. Check Balance  
6. Close Account  
7. Exit  
''')

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

class Bankaccount:
    def __init__(self):
        pass

    @staticmethod
    def search():
        while True:
            show_menu()
            try:
                choice = int(input("Enter your choice (1–7): "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            match choice:
                case 1:
                    while True:
                        name = input("Enter Full Name: ")
                        account_number = "SBI" + str(random.randint(10000000, 99999999))
                        if not name.replace(" ", "").isalpha():
                            print("Please enter alphabetical words")
                            continue
                        with open(f"{account_number}.txt", "w") as f:
                            f.write(f"Name: {name}")
                        break

                    while True:
                        account_type= input("Enter Account Type (Savings/Current): ")
                        if account_type not in ['Savings','Current']:
                            print("❌Invalid account type")
                            continue
                        with open(f"{account_number}.txt", "a") as f:
                            f.write(f"\nAccount type: {account_type}")
                        break

                    while True:
                        pin= input("Set 4-digit PIN: ")
                        if not (pin.isdigit() and len(pin)==4):
                            print("❌PIN must be a 4-digit number")
                            continue
                        hashed_pin = hash_pin(pin)
                        with open(f"{account_number}.txt", "a") as f:
                            f.write(f"\nPin: {hashed_pin }")
                        break

                    while True:
                        initial_deposit= input("Initial Deposit: Rs")
                        if initial_deposit.isdigit() and int(initial_deposit) > 0:
                            with open(f"{account_number}.txt", "a") as f:
                                f.write(f"\nBalance: {initial_deposit}")
                            print("\n✅Account created successfully")
                            print(f"Your Account number is: {account_number}")
                            with open(f"{account_number}.txt", "a") as f:
                                f.write(f"\nAccount number: {account_number}")
                            break
                        else:
                            print("❌Invalid deposit amount")
                            continue


                case 2:
                    while True:
                        num=input("Enter Account number: ")
                        if not os.path.exists(f"{num}.txt"):
                            print("Account Not Found")
                            continue


                        with open(f"{num}.txt","r") as f1:
                            lines=f1.readlines()
                        previous_balance=int(lines[3].split(":")[1])

                        while True:
                            amount = int(input("Enter Amount to Deposit: Rs"))
                            if amount>0:
                                previous_balance+=amount
                                lines[3]=f"Balance: {previous_balance}\n"
                                break
                            else:
                                print("Please enter positive amount")
                                continue

                        with open(f"{num}.txt","w") as f2:
                            f2.writelines(lines)
                        print(f"✅ Rs {amount} deposit successfully")
                        break


                case 3:
                    while True:
                        num=input("Enter Account Number: ")
                        if not os.path.exists(f"{num}.txt"):
                            print("Account Not Found")
                            continue

                        with open(f"{num}.txt","r") as f:
                            lines=f.readlines()
                        previous_balance=int(lines[3].split(":")[1])

                        while True:
                            amount = int(input("Enter Amount to Withdraw: Rs"))
                            if not amount>0:
                                print("Please enter positive amount")
                                continue
                            if amount > previous_balance:
                                print("❌ Insufficient Balance")
                                continue
                            break

                        previous_pin=lines[2].split(":")[1].strip()
                        while True:
                            entered_pin = input("Enter PIN: ")
                            if hash_pin(entered_pin)==previous_pin:
                                previous_balance -= amount
                                lines[3]=f"Balance: {previous_balance}\n"
                                break
                            else:
                                print("❌Invalid PIN")
                                continue

                        with open(f"{num}.txt","w") as f5:
                            f5.writelines(lines)
                            print(f"✅ Rs {amount} Withdrawl successfully")
                        break


                case 4:
                    while True:
                        from_account=input("From Account: ")
                        if not os.path.exists(f"{from_account}.txt"):
                            print("Account Not Found")
                            continue
                        break

                    while True:
                        to_account=input("To Account: ")
                        if not os.path.exists(f"{to_account}.txt"):
                            print("Account Not Found")
                            continue
                        break

                    with open(f"{from_account}.txt","r") as f:
                        lines=f.readlines()
                    previous_balance=int(lines[3].split(":")[1])

                    while True:
                        amount = int(input("Enter Amount to Transferred: Rs"))
                        if not amount>0:
                            print("Please enter positive amount")
                            continue
                        if amount > previous_balance:
                            print("❌ Insufficient Balance")
                            continue
                        break

                    previous_pin=lines[2].split(":")[1].strip()
                    while True:
                        entered_pin = input("Enter PIN: ")
                        if hash_pin(entered_pin)==previous_pin:
                            previous_balance -= amount
                            lines[3]=f"Balance: {previous_balance}\n"
                            break
                        else:
                            print("❌Invalid PIN")
                            continue

                    with open(f"{from_account}.txt","w") as f5:
                        f5.writelines(lines)


                    with open(f"{to_account}.txt", "r") as f:
                        lines1 = f.readlines()
                    previous_balance1 = int(lines1[3].split(":")[1])

                    previous_balance1 += amount
                    lines1[3] = f"Balance: {previous_balance1}\n"

                    with open(f"{to_account}.txt","w") as f8:
                        f8.writelines(lines1)

                        print(f"✅ Rs {amount} Transferred successfully to {to_account}")


                case 5:
                    while True:
                        num = input("Enter Account Number: ")
                        if not os.path.exists(f"{num}.txt"):
                            print("Account Not Found")
                            continue
                        break


                    with open(f"{num}.txt","r") as f:
                        lines=f.readlines()

                    previous_pin = lines[2].split(":")[1].strip()
                    while True:
                        pin = input("Enter PIN: ")
                        if hash_pin(pin) != previous_pin:
                            print("❌Invalid PIN")
                            continue
                        break

                    previous_balance3=int(lines[3].split(":")[1])
                    print(f"Balance: Rs{previous_balance3}")

                    print("✅ Balanced checked successfully")


                case 6:
                    while True:
                        num = input("Enter Account Number: ")
                        if not os.path.exists(f"{num}.txt"):
                            print("Account Not Found")
                            continue
                        break

                    with open(f"{num}.txt","r") as f:
                        lines=f.readlines()

                    previous_pin = lines[2].split(":")[1].strip()
                    while True:
                        pin = input("Enter PIN: ")
                        if hash_pin(pin) != previous_pin:
                            print("❌Invalid PIN")
                            continue
                        break

                    os.remove(f"{num}.txt")
                    print("✅ Account Closed successfully")


                case 7:
                    print('''Thank you for banking with SBI Bank \nHave a great day.''')
                    break
                case _:
                    print("❌ Invalid choice")
                    continue



bank=Bankaccount()
bank.search()
