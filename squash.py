def squash(matrix):
    """Return squashed list from list of lists"""
    return [
        y for x in matrix 
        for y in x
    ]
    
matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
print (matrix)