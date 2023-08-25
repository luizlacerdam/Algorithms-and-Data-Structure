from cyclotron import cyclotron


def test_cyclotron_without_particles_4x4():
    no_particles = "[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"
    assert cyclotron(4) == no_particles


def test_cyclotron_electron_particles_4x4():
    electron_def = "[e, e, e, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n"
    assert cyclotron("e", 4) == electron_def


def test_cyclotron_proton_particles_4x4():
    proton_def = "[p, p, p, p]\n[p, 1, 1, p]\n[p, 1, p, p]\n[p, p, p, 1]\n"
    assert cyclotron("p", 4) == proton_def


def test_cyclotron_proton_particles_6x6():
    proton_d = "[p, p, p, p, p, p]\n[p, 1, 1, 1, 1, p]\n[p, 1, 1, 1, 1, p]\n"
    proton_d += "[p, 1, 1, 1, 1, p]\n[p, 1, 1, 1, p, p]\n[p, p, p, p, p, 1]\n"
    assert cyclotron("p", 6) == proton_d


def test_cyclotron_neutron_particles_4x4():
    neutron_def = "[n, n, n, n]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n"
    assert cyclotron("n", 4) == neutron_def
