x = input().split(" ")
(print(x[0]if ord(x[0])<ord(x[1])else x[1])if "R"in x else print(x[0]if ord(x[0])>ord(x[1])else x[1])) if x[0]!=x[1] else print("D")
