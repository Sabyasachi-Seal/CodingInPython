# Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum
# of which is S (we can use as many coins of one type as we want), if it is not possible to select coins in such a way
# that they sum up to S then print '-1'.
# Example: Given coins with values 1, 3, and 5. And the sum S is 11.
# Output: 3, 2 coins of 3 and 1 coin of 5
# Input Size : N<=10000
# Example:
# INPUT
# 3 11
# 1 3 5
# OUTPUT
# 3
num, tot= list(map(int, input().split(" ")))
nums, c, tmp = sorted(list(map(int, input().split(" ")))[:num], reverse=True), 0, tot
for i in nums:
    tmp-= i if (tot-i)>0 else 0
    c+=(print(c+(2 if tot not in nums else 1), end=""), exit()) if tmp in nums else 1
print("-1", end="")
