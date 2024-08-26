from seasons import convert_time



def test_convert_time():
    assert convert_time(
        "2003-01-21") == "Eleven million, three hundred thirty-seven thousand, one hundred twenty minutes"


