def reverse(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1
def Rotate_Left(arr,d,n):
    if d == 0:
        return
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
if __name__ == '__main__':
    n = int(input())
    array = list(map(int,input().strip().split()))[:n]
    d = int(input())
    Rotate_Left(array,d,n)
    print(array)
