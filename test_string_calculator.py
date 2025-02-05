# test_string_calculator.py

import pytest
from string_calculator import StringCalculator


def test_empty_string_returns_0():
    calculator = StringCalculator()
    assert calculator.add("") == 0