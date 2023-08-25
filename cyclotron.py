def case_electron(particle, matrix_size):
    first_line = "[" + particle + ", " + (matrix_size - 2) * (particle + ", ") + particle + "]\n"
    other_lines = "[1" + (matrix_size - 2) * (", 1") + ", " + particle + "]\n"
    matrix = first_line + (matrix_size - 1) * other_lines
    return matrix


def case_proton(particle, matrix_size):
    first_line = "[" + particle + ", " + (matrix_size - 2) * (particle + ", ") + particle + "]\n"
    middle_lines = "[" + particle + (matrix_size - 2) * (", 1") + ", " + particle + "]\n"
    penultimate_line = "[" + particle + ", " + (matrix_size - 4) * "1, " + "1, " + particle + ", " +  particle + "]\n"
    last_line = "[" + particle + ", " + (matrix_size - 2) * (particle + ", ") + "1]\n"
    matrix = first_line + (matrix_size - 3) * middle_lines + penultimate_line + last_line
    return matrix


def case_neutron(particle, matrix_size):
    first_line = "[" + particle + ", " + (matrix_size - 2) * (particle + ", ") + particle + "]\n"
    lines = "[1" + (matrix_size - 2) * (", 1") + ", " + "1]\n"
    matrix = first_line + (matrix_size - 1) * lines
    return matrix 


def case_none(matrix_size):
    lines = "[1" + (matrix_size - 2) * (", 1") + ", " + "1]\n"
    matrix = lines + (matrix_size - 1) * lines
    return matrix


def cyclotron(particle, matrix_size=4):
    if particle is None:
        return case_none(matrix_size)
    case = {
        "e": case_electron(particle, matrix_size),
        "p": case_proton(particle, matrix_size),
        "n": case_neutron(particle, matrix_size)
    }
    return case[particle]


print(cyclotron(None, 6))
