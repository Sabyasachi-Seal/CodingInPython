def sq(n):
    try:
        square = [[0 for a in range(n)]for b in range(n)]
        i, j, number = n//2, n-1, 1
        while number <= n**2:
            if i < 0 and j == n:
                i, j = 0, n-2
            elif i < 0 and j != n:
                i = n - 1
            elif j == n and i >= 0:
                j = 0
            elif square[i][j] != 0:
                i, j = i+1, j-2
                continue
            else:
                square[i][j] = number
                i, j, number = i-1, j+1, number+1
        for i in range(0, n):
            for j in range(0, n):
                print(square[i][j], end=" ")
            print()
        print(f"Sum = ", int(n*((n**2)+1)/2))
    except IndexError:
        print("Odd Number Only. Try again.")


sq(n=int(input("> ")))
