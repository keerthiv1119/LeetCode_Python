Length = int(input())
array = list(map(int,input().strip().split()))[:Length]
Sum = int(input("Enter the Sum Value : "))
dictionary = {}
position = 0
while(position < Length):
    if Sum - array[position] not in dictionary:
        dictionary[array[position]] = position
        position += 1
    else:
        return dictionary[Sum - array[position]],position
        
