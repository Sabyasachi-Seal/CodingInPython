def solve (a, b, n):
    if(n%3==0): return a;
    elif(n%3==1): return b;
    else: return a^b


t = (int)(input())
ans = []
for _ in range(t):
    a, b, n = map(int, input().split())
    ans.append(str(solve(a, b, n)))
print("\n".join(ans))