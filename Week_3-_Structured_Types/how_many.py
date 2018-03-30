def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here

    # Save dictionary values in variable animal_value
    animal_value = aDict.values()
    
    # Animal counter to count each element in list
    animal_counter_in_list = 0

    # Loop through the list and an int (len(i) to an int (animal counter) to find out how
    # many elements are in the value of the dictionary 
    for i in animal_value:
        animal_counter_in_list += len(i)

    return animal_counter_in_list

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))