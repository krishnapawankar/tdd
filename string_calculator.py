# string_calculator.py

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        return int(numbers)  # If there's only one number, convert and return