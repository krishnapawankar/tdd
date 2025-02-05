# test_string_calculator.py

import pytest
from string_calculator import StringCalculator


def test_empty_string_returns_0():
    calculator = StringCalculator()
    assert calculator.add("") == 0


def test_single_number_returns_value():
    calculator = StringCalculator()
    assert calculator.add("1") == 1


def test_two_numbers_comma_delimited():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3


def test_unknown_amount_of_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2,3,4") == 10


def test_newline_delimiter():
    calculator = StringCalculator()
    # "1\n2,3" => 6
    assert calculator.add("1\n2,3") == 6


def test_custom_delimiter_single_char():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3


def test_negative_numbers_throw_exception():
    calculator = StringCalculator()
    with pytest.raises(Exception) as ex:
        calculator.add("1,-2,3")
    assert "Negatives not allowed:" in str(ex.value)
    assert "-2" in str(ex.value)
