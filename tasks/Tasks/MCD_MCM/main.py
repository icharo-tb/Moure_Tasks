def greatest_common_divisor(a,b):
    # Euclides Algorithm
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b,a%b)    
pass

print(greatest_common_divisor(60,48))

def least_common_multiple(a,b):
    if a > b:
        a,b = b,a
    for i in range(b,a*b+1,b):
       if i%a == 0:
        return i 
pass

print(least_common_multiple(3,4))