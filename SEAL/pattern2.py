rows = int(input("Enter The Number Of Rows: "))
columns = 2 * rows - 1
i = 0
while i < rows:
    j = 0
    while j < columns:
        if ((columns // 2) - i <= j <= (columns // 2) + i):
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1

i = 1
while i < rows:
    j = 0
    while j < columns:
        if (i <= j <= columns - 1 - i):
            print("*", end="")
        else:
            print(" ", end="")

        j += 1
    print(" ")
    i += 1