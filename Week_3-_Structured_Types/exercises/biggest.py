def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here

    biggest_key = 0
    result = None # if there are no key values, then the result would be None,
                  # if not then the result would print the key with the biggest value

    for key in aDict.keys():
        # compare different key lengths and the greatest key length gets returned
        if len(aDict.keys()) >= biggest_key:
            result = key # Save the key in the variable to return later if the conditions are met
            biggest_key = len(aDict.keys()) # Save the length count of each iterating key
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))