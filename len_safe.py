def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        return len(object)
    except TypeError:
        return -1

animals = ['dog', 'cat', 'bird', 'cat', 'fish']
print (len_safe(animals))