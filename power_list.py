def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
    new_list=[
        numbers**index
        for index,numbers in enumerate(numbers,start=0)
    ]
    return new_list
    
print (power_list([2, 2, 2, 2, 2, 2]))
   