def numtowords(num):  
    if num == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    result = ""  
    if num>= 1000:  
        result += ones[num // 1000] + " thousand "  
        num %= 1000  
    if num>= 100:  
        result += ones[num // 100] + " hundred "  
        num %= 100  
    if num>= 10 and num<= 19:  
        result += teens[num - 10] + " "  
        num = 0  
    elif num>= 20:  
        result += tens[num // 10] + " "  
    num %= 10  
    if num>= 1 and num<= 9:  
        result += ones[num] + " " 
    return result.strip()  

if __name__ == "__main__":
    print(numtowords(9213))
    print(numtowords(1312))
    print(numtowords(29))
