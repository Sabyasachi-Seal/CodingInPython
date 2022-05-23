# n, k = list(map(int, input().split(" ")))
# arr = list(map(int, input().split(" ")))
n = 5
k = 5
arr = [3, 5, 2, 5, 1]
ans = {};
for i in range(0, n+1):
    ans[i] = 0;
for i in range(0, k-1, 1):
    ans[arr[i]]+=1
    ans[arr[i+1]-1]+=1
    # print(arr[i], arr[i+1]-1)
ans[arr[k-1]]+=1
ans = sorted((value, key) for (key,value) in ans.items())
[print(i[1]) for i in ans[2:]]