import math
def array_rotate(arr,n,d):
    sets = math.gcd(n,d)
    for i in range(sets):
        j = i
        temp = arr[i]
        while True:
            k = (j + d) % n
            if k == i :
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
n = int(input())
array = list(map(int,input().strip().split()))[:n]
d = int(input())
array_rotate(array,n,d)
print(array)
