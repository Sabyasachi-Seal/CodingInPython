# Happy New Year

def add(num1, num2):
    result = num1 + num2
    return result


def sub(num1, num2):
    result = abs(num1 - num2)
    return result


def main():
    valid = False
    while not valid:
        try:
            num1 = float(input("Enter Number 1:"))
            num2 = float(input("Enter Number 2:"))
            mode = input("Enter the mode(add/subtract): ").lower()
            valid = True
            if mode == "add":
                result = add(num1, num2)
            elif mode == "subtract":
                result = sub(num1, num2)
            print(f"Result = {result}")
            print()
        except ValueError:
            print("Invalid Value!!!, try again")
            print()
        except NameError:
            print("Invalid Mode!!!, try again")
            print()


USE = True
while USE:
    mood = input("Would you like to use the calculator?(YES/NO) : ").lower()
    if mood == "yes":
        main()
    elif mood == "no":
        USE = False
        print("Have a Great Day!!!")
    else:
        print("Command unrecognised !!! Try again.")
