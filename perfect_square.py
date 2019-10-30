def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    num = number**0.5
    if num.is_integer():
        return True
    else:
        return False


number = int((input("Input number to see is it a perfect square:")))
print(is_perfect_square(number))
