def Reverse_Integer(x):
    String_x = str(x)
    Reverse_x = String_x[::-1]
    if Reverse_x[-1] != '-':
        Result = int(Reverse_x)
    else:
        Result = int(Reverse_x[:-1]) * -1
    if Result >= -2 ** 31 and Result < 2 ** 31:
        return Result
    else:
        return 0
Number = int(input())
print(Reverse_Integer(Number))
