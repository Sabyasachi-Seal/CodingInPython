ans = []
for i in range(int(input())):
    series = input().split(" ")
    ind, eng = series.count("1"), series.count("2")
    ans.append("India" if ind>eng else "England" if ind!=eng else "Draw")
print("\n".join(ans), end="")
