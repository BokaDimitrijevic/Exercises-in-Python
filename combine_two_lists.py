def combine_lists(one, two):
    """Take 2 lists as input and return a new list consisting of the elements
        of the first list followed by the elements of the second list"""
    return one + two
    
first = [1, 2, 3]
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
new = combine_lists(first, fruits)
print (new)
    