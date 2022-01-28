# Write a function called fizz_buzz that takes a number.
#
#     If the number is divisible by 3, it should return “Fizz”.
#     If it is divisible by 5, it should return “Buzz”.
#     If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#     Otherwise, it should return the same number.

def inputter():
    num = int(input("enter number: "))
    return num


def fizzbuzz(number):
    if number%3 == 0 and number%5 != 0:
        return "FIZZ"
    elif number%5 == 0 and number%3 != 0:
        return "BUZZ"
    elif number%3 == 0 and number%5 ==0:
        return "FIZZBUZZ"
    else:
        return number


def main():
    num1 = inputter()
    print(fizzbuzz(number=num1))


main()


