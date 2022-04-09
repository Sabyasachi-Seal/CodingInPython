def getPhoneNumber(s):
    # Write your code here
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new = {}
    for index, num in enumerate(numbers):
        new[num] = index
        
    numbers = s.split(" ")
    s = ""
    for index, nums in enumerate(numbers):
        if nums == "double":
            for i in range(1):
                s += str(new[numbers[index+1]])
        elif nums == "triple":
            for i in range(2):
                s += str(new[numbers[index+1]])
        else:
            s += str(new[nums])
    return s

print(getPhoneNumber("zero nine triple five two"))