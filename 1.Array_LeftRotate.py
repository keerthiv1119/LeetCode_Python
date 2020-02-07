def array_rotation(arr,n,d):
    for i in range(d):
        RotateOne(arr,n)
def RotateOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i],end = ' ')
n = int(input("Enter the length"))
a = list(map(int,input().strip().split()))[:n]
d = int(input())
array_rotation(a,n,d)
print_array(a)
