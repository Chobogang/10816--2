n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))
arr = []
for i in arrM :
     arr.append(arrN.count(i))

print(arr)