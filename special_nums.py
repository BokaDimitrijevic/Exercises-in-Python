def special_nums():
    """Return list of numbers from 1 to 300 that are divisible by 10 and 6"""
    return [num for num in range(1,301) if num % 30 == 0]
    
list_result = special_nums()
print (list_result)