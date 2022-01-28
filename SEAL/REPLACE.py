a = input()
x = input().split(" ")
for i in range(0, len(x), 2):
    if i==len(x)-1 and len(x)%2!=0:
        break
    temp = x[i]
    x[i] = x[i+1]
    x[i+1] = temp
print(*x, end="")