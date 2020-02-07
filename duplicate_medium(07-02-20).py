def Duplicate(arr):
    return int((sum(arr) - sum(set(arr))) / (len(arr) - (len(set(arr)))))
arr = [1,1,1,3,2]
print(Duplicate(arr))
