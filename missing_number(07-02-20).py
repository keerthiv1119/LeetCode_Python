def missed(arr):
    Sum = 0
    Total = 0
    for i in range(len(arr)):
        Sum += arr[i]
    for j in range(len(arr)+1):
        Total += j
    print(Sum)
    print(Total)
    return Total - Sum
a =[3,0,1]
print(missed(a))
