def cyclotron(particle, matrix_size):
    matrix = ""
    for i in range(matrix_size):
        matrix += "["
        for j in range(matrix_size):
            if j == matrix_size - 1:
                matrix += "1"
            else:
                matrix += "1" + ", "
        matrix += "]"
        matrix += "\n"
    return matrix


print(cyclotron("e", 4))
