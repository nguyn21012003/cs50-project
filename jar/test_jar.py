from jar import Jar


def test_init():
    jar = Jar(12)
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar2.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert jar.size == 1


def test_draw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(6)
    jar.withdraw(2)
    assert jar.size == 4
