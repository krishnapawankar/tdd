# string_calculator.py

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        # Replace newline with comma, then split on comma
        numbers = numbers.replace("\n", ",")
        parts = numbers.split(",")

        return sum(int(n) for n in parts if n)