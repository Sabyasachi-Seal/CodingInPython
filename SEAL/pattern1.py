# Write a function called show_stars(rows). If rows is 5, it should print the following:
#
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
limit = int(input("Enter limit: "))
lim = 2*limit - 1
for i in range(1, (lim+2), 2):
    print(" " * (limit-i//2) + "*" * i)
for i in range((lim-2), 0, -2):
    print(" " * (limit-i//2) + "*" * i)
