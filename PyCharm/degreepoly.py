# https://www.codechef.com/MAY222C/problems/DPOLY
cases = int(input())
nterms, terms = [], []
for case in range(cases):
    nterms.append(int(input()))
    terms.append(list(map(int, input().split(" "))))

for case in range(cases):
    for index, term in enumerate(terms[case][::-1]):
        if(term != 0):
            print(nterms[case] - 1 - index)
            break