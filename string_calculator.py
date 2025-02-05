# string_calculator.py

import re

class StringCalculator:
    def __init__(self):
        self._call_count = 0

    def get_called_count(self) -> int:
        return self._call_count

    def add(self, numbers: str) -> int:
        self._call_count += 1

        if not numbers:
            return 0

        # Default delimiter(s):
        delimiters = ["," , "\n"]

        # Check if string starts with //
        if numbers.startswith("//"):
            # Check for bracketed delimiters:
            # e.g. //[***]\n
            pattern = r"^//\[(.+)\]\n"
            match = re.match(pattern, numbers)
            if match:
                custom_delim = match.group(1)  # e.g. ***
                # Split off the first line
                _, numbers = numbers.split("\n", 1)
                # Add the custom delimiter to the list
                delimiters = [custom_delim, "\n", ","]
            else:
                # Single-char logic from earlier (//;\n)
                delimiter = numbers[2]
                # Remove the '//' and delimiter + newline
                numbers = numbers.split("\n", 1)[1]
                delimiters = [delimiter, "\n", ","]

        # Build a regex pattern to split on *any* of the delimiters
        # We escape them in case they have special regex characters
        delimiters_escaped = [re.escape(d) for d in delimiters]
        split_pattern = "|".join(delimiters_escaped)

        parts = re.split(split_pattern, numbers)

        negatives = []
        total = 0
        for p in parts:
            if not p.strip():
                continue
            value = int(p)
            if value < 0:
                negatives.append(value)
            elif value <= 1000:
                total += value

        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")

        return total
