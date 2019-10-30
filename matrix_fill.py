def matrix_fill(rows,cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    return [[x for x in range(1,rows*cols+1)][i:i+cols] for i in range(0,rows*cols,cols)]
    
my_matrix = matrix_fill(3, 4)
print (my_matrix)

    

