import sys
n = int(input())
arrN = list(map(int, sys.stdin.readline().split()))
m = int(input())
arrM = list(map(int, sys.stdin.readline().split()))
arr = []
for i in arrM :
     arr.append(arrN.count(i))

print(arr)