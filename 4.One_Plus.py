def Plus(arr):
    if arr[-1] == 9:
        number = int("".join(map(str,arr)))
        number += 1
        Sum_List = [int(x) for x in str(number)]
        return Sum_List
    else:
        arr[-1] += 1
        return arr
n = int(input())
Array = list(map(int,input().strip().split()))[:n]
print(Plus(Array))
