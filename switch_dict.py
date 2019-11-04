def switch_dict(dictionary):
    """Return a new dictionary with keys and values switched"""
    return {
        value: key 
        for key, value in dictionary.items()
    }
    

data = {'a': 2, 'b': 5, 'c': 6}
switched = switch_dict(data)
print(switched)
 