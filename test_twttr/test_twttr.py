from twttr import shorten

import pytest


def test_short():
    assert shorten("Twitter").strip() == "Twttr"
    assert shorten("What's your name?").strip() == "Wht's yr nm?"
    assert shorten("CS50").strip() == "CS50"
    assert shorten("PYTHON").strip() == "PYTHN"
