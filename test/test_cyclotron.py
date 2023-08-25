from cyclotron import cyclotron


def test_cyclotron_electron_particles_4x4():
    electron_def = "[e, e, e, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n"
    assert cyclotron("e", 4) == electron_def


def test_cyclotron_proton_particles_4x4():
    proton_def = "[p, p, p, p]\n[p, 1, 1, p]\n[p, 1, p, p]\n[p, p, p, 1]\n"
    assert cyclotron("p", 4) == proton_def


def test_cyclotron_proton_particles_6x6():
    proton_def = "[p, p, p, p, p, p]\n[p, 1, 1, 1, 1, p]\n[p, 1, 1, 1, 1, p]\n[p, 1, 1, 1, 1, p]\n[p, 1, 1, 1, p, p]\n[p, p, p, p, p, 1]"
    assert cyclotron("p", 6) == proton_def
