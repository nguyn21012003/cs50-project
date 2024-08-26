from plates import is_valid


def test_is_valid():
    assert bool(is_valid("CS50")) == True
    assert bool(is_valid("50")) == False
    assert bool(is_valid("CS05")) == False
    assert bool(is_valid("CS50P")) == False
    assert bool(is_valid("PI3.14")) == False
    assert bool(is_valid("H")) == False
    assert bool(is_valid("OUTATIME")) == False
