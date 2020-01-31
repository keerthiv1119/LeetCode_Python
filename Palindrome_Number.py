Number = int(input())
def pali(n):
    String_Number = str(Number)
    Reverse_String = String_Number[::-1]
    if String_Number == Reverse_String:
        return True
    else:
        return False
output = pali(Number)
print(output)
