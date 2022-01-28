def calc(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2


def inputter():
    num1 = int(input("1> "))
    num2 = int(input("2> "))
    return num1, num2


def main():
    num1,num2 = inputter()
    print(calc(num1 , num2))


main()