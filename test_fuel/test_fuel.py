from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert('3/4') == 75
    assert convert('4/5') == 80


def test_convert_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("2/0")
    with pytest.raises(ValueError):
        convert("2/1")
        convert("cat/1")
        convert("cat/dog")
        convert("1/dog")


def test_gauge():
    assert gauge(convert("1/2")) == "50%"
    assert gauge(convert("3/4")) == "75%"
    assert gauge(convert("1/1000")) == "E"
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert('1/1')) == "F"
    assert gauge(convert('99/100')) == "F"
    assert gauge(convert('2/3')) == "67%"
