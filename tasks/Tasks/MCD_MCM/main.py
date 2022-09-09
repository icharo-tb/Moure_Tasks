def greatest_common_divisor(a,b):
    # Euclides Algorithm
    if a<b:
        remainder_a = b%a
        remainder_b = a%remainder_a
    elif a>b:
        remainder_a = a%b
        remainder_b = b%remainder_a

    if b%remainder_a == 0:
        gcd = remainder_a
    elif b%remainder_a != 0:
        gcd = gcd = remainder_a%remainder_b
    
    #return f"Quotient of {a} is {quotient_a}{nl}Remainder of {a} is {remainder_a}"
    return f"GCD of {a} and {b} is {gcd}"
pass
print(greatest_common_divisor(34,12))

def least_common_multiple(a,b):
    pass