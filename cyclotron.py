def case_electron():
    return "[e, e, e, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n"


def case_proton():
    return "[p, p, p, p]\n[p, 1, 1, p]\n[p, 1, p, p]\n[p, p, p, 1]\n"


def case_neutron():
    return "[n, n, n, n]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"


def case_none():
    return "[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"


def cyclotron(particle=None, matrix_size=4):
    matrix = ""
    case = {
        "e": case_electron(),
        "p": case_proton(),
        "n": case_neutron(),
        None: case_none()
    }
    matrix += case[particle]
    return matrix


print(cyclotron(None, 4))