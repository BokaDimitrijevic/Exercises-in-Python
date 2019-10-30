def str_together(in_string):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    return " - ".join(map(str,in_string))
    
fruits = ['Orange', 'Lemon', 'Lime', 'Cherry', 'Peach', 'Apricot']
fruit_string = str_together(fruits)
print(fruit_string)
