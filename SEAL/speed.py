# Write a function for checking the speed of drivers. This function should have one parameter: speed.
#
#     If speed is less than 70, it should print “Ok”.
#     Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the
#     total number of demerit points. For example,
#     if the speed is 80, it should print: “Points: 2”.
#     If the driver gets more than 12 points, the function should print: “License suspended”

def checker(speed):
    if speed <= 70:
        return "ok"
    else:
        points = int((speed - 70)/5)
        return points


def inputter():
    speed = int(input("enter speed: "))
    return speed


def main():
    speed = inputter()
    while speed > 70:
        points = checker(speed)
        if points >= 12:
            print("License Expired")
            break
        print(f"Points: {points}")
        break
    else:
        print(checker(speed))


main()
