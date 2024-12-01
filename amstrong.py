import math

def isAmstrong( value ):
    sum = 0
    
    for i in str(value):
        sum += math.pow(int(i), len(str(value)))
        
    return sum == value

print(isAmstrong(153))
print(isAmstrong(9474))
print(isAmstrong(1741725))