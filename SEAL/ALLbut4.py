nums, resolved = input(), []
for number in nums.split(" "):
    if list(number)[len(number)-1] != "4":
        resolved.append(number)
print(*resolved, end="")
