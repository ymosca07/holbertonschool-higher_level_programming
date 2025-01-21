def print_matrix_integer(matrix=[[]]):
    
    i = 0
    
    for i in matrix:
        print(" ".join("{:d}".format(num) for num in i))
