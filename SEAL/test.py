n = int(input())
for i in range(1, n+1, 2):
    print(" "*((n-i)//2)+f"{i}"*i)
