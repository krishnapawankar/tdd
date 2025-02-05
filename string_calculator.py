# string_calculator.py

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","
        # Check if we have a custom delimiter
        if numbers.startswith("//"):
            # e.g. "//;\n1;2"
            # 1) Extract custom delimiter after '//'
            delimiter = numbers[2]
            # 2) The numbers start after the newline
            numbers = numbers.split("\n", 1)[1]  # everything after the first newline
        # Now we can replace newlines with our "delimiter" as well
        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(delimiter)

        return sum(int(n) for n in parts if n)