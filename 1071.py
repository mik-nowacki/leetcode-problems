# str1 = "ABCABC"
# str2 = "ABC"

str1 = "ABABABAB"
str2 = "ABAB"

def gcd(str1, str2):
    i = 0
    j = 0
    divisor = str2[j]
    best_div = ""
    while j < len(str2):
        step = len(divisor)
        if str1[i:i+step] == divisor:  # go further 
            i += step
        elif i > len(str1)-1:  # end of str1
            best_div = divisor
            i = 0
            j += 1
            if j > len(str2)-1:  # positive result
                return best_div
            divisor += str2[j]
        else:    # add chars
            i = 0
            j += 1
            if j > len(str2)-1:  # negative result
                return ""
            divisor += str2[j]

print(gcd(str1, str2))

