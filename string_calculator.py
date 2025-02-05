# string_calculator.py

class StringCalculator:
    def add(self, numbers: str) -> int:
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
            # raise an exception with all the negatives
            negatives_str = ",".join(str(x) for x in negatives)
            raise Exception(f"Negatives not allowed: {negatives_str}")

        return total
