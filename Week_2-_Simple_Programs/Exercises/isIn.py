def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    # Base case #1: If aStr is empty, we did not find the char.
    if len(aStr) == 0:
        return False
    # Base case #2: if aStr is of length 1, just see if the chars are equal
    elif len(aStr) == 1:
        return char == aStr[0]

    middle = (len(aStr)) // 2 # "//" is used to convert a float to an int
    upper_half = aStr[middle:] # middle: is from the middle to the end to find the upper_half of the string
    print(upper_half)
    lower_half = aStr[:middle] # :middle is from the beginning to the middle to find the lower_half of the string

    # recursive algorithm
    if char == aStr[middle]:
        return True
    # Bisectional search
    elif char < aStr[middle]:
        return isIn(char, lower_half) # aStr is replaced by lower_half value to cut out the upper half
    else:
        return isIn(char, upper_half)

print(isIn('g', 'abcccdeeeefggghiiiijkkklllmmmoooppp'))
print(isIn('z', 'abcccdeeeefggghiiiijkkklllmmmoooppp'))



