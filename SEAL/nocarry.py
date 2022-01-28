a, b = input().split(" ")
total = ""
for i in range(1, 3):
    total+=str(int(a[-i])+int(b[-i]))if (int(a[-i])+int(b[-i]))<10else str(int(a[-i])+int(b[-i])-10)
print(total[::-1], end="")
