n=int(input())

for i in range(n):
    rows, columns = list(map(int,input().split()))

    print("Case #",i+1,":",sep="")
    
    print("..",end='')
    
    for i in range(columns-1):
        print("+-",end='')
    print("+")
    
    print("..",end='')
    
    for i in range(columns-1):
        print("|.",end='')
    print("|")
    
    for j in range(rows):
        for k in range(columns):
            print("+-",end='')
        print("+")

        if j<rows-1:
            for k in range(columns):
                print("|.",end='')
            print("|")