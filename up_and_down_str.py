def string_low_up(in_string):
    """Given a string, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters are upper case.
        Return the silly case string."""
    return in_string.title().swapcase()
    
silly_string = string_low_up("This is a string")
print(silly_string)
