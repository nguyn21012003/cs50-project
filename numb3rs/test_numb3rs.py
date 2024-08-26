from numb3rs import validate


def test_validate():
    assert bool(validate("255.255.255.255")) == True
    assert bool(validate("512.512.512.512")) == False
    assert bool(validate("cat.dog")) == False
    assert bool(validate("cat.")) == False
    assert bool(validate("1.2.3.1000")) == False
    assert bool(validate("256.255.255.255")) == False
    assert bool(validate("8.8.8")) == False
    assert bool(validate("10.10.10.10.10")) == False
    assert bool(validate("75.456.76.65")) == False
    assert bool(validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) == False
