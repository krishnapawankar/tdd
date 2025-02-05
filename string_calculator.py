# string_calculator.py

class StringCalculator:
    def __init__(self):
        self._call_count = 0

    def get_called_count(self) -> int:
        return self._call_count

    def add(self, numbers: str) -> int:
        self._call_count += 1

        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers.split("\n", 1)[1]

        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(delimiter)

        negatives = []
        total = 0
        for p in parts:
            if not p.strip():
                continue
            value = int(p)
            if value < 0:
                negatives.append(value)
            else:
                total += value

        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")

        return total
