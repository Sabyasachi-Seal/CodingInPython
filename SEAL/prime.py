# Write a function that prints all the prime numbers between 0 and limit where limit
# is a parameter.


def inputter():
    lim = int(input("enter limit: "))
    return lim


def primmer(limit):
    for number in range(0, limit+1):
        i=2
        while i in range(2, number):
            if number % i == 0:
                break
            i += 1
        else:
            print(number)


def main():
    num = inputter()
    primmer(limit=num)


main()
