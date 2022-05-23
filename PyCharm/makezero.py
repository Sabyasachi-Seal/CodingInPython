# https://www.codechef.com/MAY222C/problems/MAKEZERO
cases = int(input())
nele, ele = [], []
for case in range(cases):
    nele.append(int(input()))
    ele.append(list(map(int, input().split(" "))))

for case in range(cases):
    ele[case] = sorted(ele[case])
    if(ele[case][-1] % 2 == 0):
        ele[case][-1] //= 2
        if(ele[case][-2] != 0):
            ele[case][-2] += 1
    else:
        ele[case][-1] //= 2
        ele[case][-1] += 1
    print(ele[case][-1])
    