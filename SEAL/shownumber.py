# Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0
# and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
#
#     0 EVEN
#     1 ODD
#     2 EVEN
#     3 ODD

def num_type(num):
    if num % 2 != 0:
        return "ODD"
    else:
        return "EVEN"


def show_numbers(limit):
    for number in range(0, limit+1):
        print(f"{number} {num_type(num = number)}")


def main():
    lim = int(input("enter limit: "))
    show_numbers(limit=lim)


main()
