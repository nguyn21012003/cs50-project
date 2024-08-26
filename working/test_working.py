from working import convert
import pytest


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:01 AM to 5:20 PM") == "09:01 to 17:20"
    assert convert("9:01 PM to 5:20 AM") == "21:01 to 05:20"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5")
    with pytest.raises(ValueError):
        convert("9:70 AM to 5")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM 17:00 PM")
    with pytest.raises(ValueError):
        convert("100:720 AM 20007:0231 PM")
    with pytest.raises(ValueError):
        convert("9 AM5 PM")
    with pytest.raises(ValueError):
        convert("9:72 to 6:30")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:72 to 6:30")
