# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def summer(limit):
    summed = 0
    print("numbers are:-")
    for number in range(0, limit+1):
        if number % 5 == 0 or number % 3 == 0:
            print(number)
            summed += number
    return summed


def main():
    lim = int(input("enter limit: "))
    print(f"sum = {summer(limit=lim)}")


main()
