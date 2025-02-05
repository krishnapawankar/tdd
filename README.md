# String Calculator TDD Kata

A Python implementation of the String Calculator Kata, developed using **Test-Driven Development (TDD)** and **pytest**.

---

## 1. Overview

This repo contains a `StringCalculator` class with an `add()` method that sums numbers from a string, fulfilling the following **requirements**:

1. An empty string returns `0`.
2. One or two numbers (comma delimited) return their sum.
3. It handles an **unknown** amount of numbers.
4. Newlines (`\n`) can also be used as delimiters.
5. Supports **custom delimiters** in the form `//<delim>\n`.
6. Throws an exception for **negative** numbers (listing all negatives).
7. **Ignore** numbers greater than 1000.
8. Supports **delimiters of any length** (e.g. `//[***]\n1***2***3`).
9. Supports **multiple custom delimiters** (e.g. `//[*][%]\n1*2%3`).
10. Has a `get_called_count()` method to track how many times `add()` was called.

All these features are **tested** with **pytest** in `test_string_calculator.py`.

---

## 2. Project Structure

    tdd/
    ├── string_calculator.py         # Production code implementing StringCalculator
    ├── test_string_calculator.py    # Unit tests using pytest
    └── README.md                    # This file

---

## 3. Environment Setup

Below are instructions using a **virtual environment** named `myenv` (you can choose any name you like):

1. **Clone** or **download** this repository.
2. Open a terminal and **create** the virtual environment:
   ```bash
   python -m venv myenv
3. Activate the virtual environment:
    ```bash
    Windows:
    myenv\Scripts\activate
    
    macOS/Linux:
    source myenv/bin/activate
4. Install dependencies (mainly pytest):
    ```bash
   pip install pytest
    
---

## 4. Running the Tests

### With your environment activated, from the tdd/ folder run:
```bash
    pytest
    
    You should see an output showing all tests passing, for example:

    ================= test session starts =================
    collected 13 items
    
    test_string_calculator.py .............
    
    ================= 13 passed in 0.05s ================

    If you want more detailed output:

    pytest -v

    =================================================================== test session starts ===================================================================
    platform win32 -- Python 3.11.3, pytest-8.3.4, pluggy-1.5.0 -- E:\tdd\myenv\Scripts\python.exe
    cachedir: .pytest_cache
    rootdir: E:\tdd\tdd
    collected 13 items
    
    test_string_calculator.py::test_empty_string_returns_0 PASSED                                                                                        [  7%]
    test_string_calculator.py::test_single_number_returns_value PASSED                                                                                   [ 15%]
    test_string_calculator.py::test_two_numbers_comma_delimited PASSED                                                                                   [ 23%]
    test_string_calculator.py::test_unknown_amount_of_numbers PASSED                                                                                     [ 30%]
    test_string_calculator.py::test_newline_delimiter PASSED                                                                                             [ 38%]
    test_string_calculator.py::test_custom_delimiter_single_char PASSED                                                                                  [ 46%]
    test_string_calculator.py::test_negative_numbers_throw_exception PASSED                                                                              [ 53%]
    test_string_calculator.py::test_multiple_negatives_throw_exception PASSED                                                                            [ 61%]
    test_string_calculator.py::test_get_called_count PASSED                                                                                              [ 69%]
    test_string_calculator.py::test_ignore_numbers_greater_than_1000 PASSED                                                                              [ 76%]
    test_string_calculator.py::test_delimiter_of_any_length PASSED                                                                                       [ 84%]
    test_string_calculator.py::test_multiple_delimiters PASSED                                                                                           [ 92%]
    test_string_calculator.py::test_multiple_long_delimiters PASSED                                                                                      [100%]
    
    =================================================================== 13 passed in 0.06s ====================================================================
```
---


## 5. Test-Driven Development Approach

### We used TDD to build this step by step:

Write a failing test for a new requirement.
Implement the minimal code to pass that test.
Refactor if needed, ensuring tests remain green.
Commit frequently after each step.
Example Commit Sequence
1. Test & implement empty string → returns 0.
2. Test & implement single number.
3. Test & implement two numbers.
4. Test & implement unknown amount of numbers.
5. Test & implement newline support.
6. Test & implement custom delimiter.
7. Test & implement negative numbers exception.
8. Test & implement get_called_count().
9. Test & implement ignoring > 1000.
10. Test & implement any length delimiter.
11. Test & implement multiple delimiters.
12. Test & implement multiple multi-char delimiters.
13. Test & implement multiple long delimiters. 
Refer to the commit history to see each stage of development.

---

## 6. Example Usage

### If you want to try StringCalculator interactively:

Activate the virtual environment.
Launch a Python interpreter:
```bash
    python
    >>> from string_calculator import StringCalculator
    >>> calc = StringCalculator()
    >>> calc.add("1,2")
    3
    >>> calc.add("1\n2,3")
    6
    >>> calc.add("//;\n1;2;3")
    6
    >>> calc.get_called_count()
    3
```

---

