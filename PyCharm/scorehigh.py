# https://www.codechef.com/MAY222C/problems/HIGHSCORE
cases = int(input())
qs, opts = [], []
for case in range(cases):
    qs.append(int(input()))
    opts.append(list(map(int, input().split(" "))))

for case in range(cases):
    print(max(opts[case]))