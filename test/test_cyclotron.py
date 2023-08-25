from cyclotron import cyclotron


def test_cyclotron_electron_particles_4x4():
    electron_def = "[e, e, e, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n[1, 1, 1, e]\n"
    assert cyclotron("e", 4) == electron_def
