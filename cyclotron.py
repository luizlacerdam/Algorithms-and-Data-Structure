def case_electron(matrix_size):
    matrix = ""
    first_line = "[e, " + (matrix_size - 2) * ("e" + ", ") + "e]\n"
    other_lines = "[1" + (matrix_size - 2) * (", 1") + ", e]\n"
    matrix += first_line + (matrix_size - 1) * other_lines
    return matrix


def case_proton(matrix_size):
    return "[p, p, p, p]\n[p, 1, 1, p]\n[p, 1, p, p]\n[p, p, p, 1]\n"


def case_neutron(matrix_size):
    return "[n, n, n, n]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"


def case_none():
    return "[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"


def cyclotron(particle=None, matrix_size=4):
    matrix = ""
    case = {
        "e": case_electron(matrix_size),
        "p": case_proton(matrix_size),
        "n": case_neutron(matrix_size),
        None: case_none()
    }
    matrix += case[particle]
    return matrix


print(cyclotron("e", 4))
