def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = min(a, b)
    while divisor > 1:
        # finding gcd
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        # decreasing divisor until > 1 then loop will break
        divisor -= 1

    # if the if statement is false, will return divisor which is 1
    return divisor

print(gcdIter(9, 12))