# string_calculator.py

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if "," in numbers:
            nums = numbers.split(",")
            return sum(int(n) for n in nums)
        else:
            return int(numbers)     # If there's only one number, convert and return
