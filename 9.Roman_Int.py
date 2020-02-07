def roman_int(s):
    dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    '''
    s = s.replace("IV","IIII").replace("IX","VIIII")
    s = s.replace("XL","XXXX").replace("XC","LXXXX")
    s = s.replace("CD","CCCC").replace("CM","DCCCC")
    numeral = 0
    for i in s:
        numeral += dictionary[i]
    return numeral
    '''
    output = 0
    prev = 0
    for i in s[::-1]:
        if dictionary[i] >= prev:
             output += dictionary[i]
        else:
            output -= dictionary[i]
        prev = dictionary[i]
    return output
Roman = input()
print(roman_int(Roman))
