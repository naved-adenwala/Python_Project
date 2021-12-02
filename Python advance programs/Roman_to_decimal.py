#dictionary
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

def RomanNumeralToDecimal(num):
    #calculating number
    sum = 0
    #looping each roman number it will run till len of romam number
    for i in range(len(num) - 1):
        first = num[i]
        second = num[i + 1]
        #if first num is less then second then it will be subtract from sum
        if roman[first] < roman[second]:
            sum -= roman[first]
        #else it will be added in first number
        else:
            sum += roman[first]
    #it will be added in sum using indexing
    sum += roman[num[-1]]
    return sum

#calling function
print(RomanNumeralToDecimal("VI"))