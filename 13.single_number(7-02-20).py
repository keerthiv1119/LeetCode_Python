def Single(arr):
    dictionary = {}
    for i in range(len(arr)):
        count = 1
        if arr[i] not in dictionary:
            dictionary[arr[i]] = count
        else:
            dictionary[arr[i]] = count + 1
    #return min(dictionary,key = dictionary.get())
    return dictionary
arr = [1,1,2]
print(Single(arr))
