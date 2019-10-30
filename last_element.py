def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    return sequence[-n:]

numbers = [41, 25, 54, 15, 76, 68, 32, 38]
print (last_n_elements(numbers, 4))