n = int(input())
array = list(map(int,input().strip().split()))[:n]
d = int(input())
while(d>0):
    array.insert(0,array.pop())
    d = d - 1
print(array)
