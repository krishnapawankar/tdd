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

        # Default delimiters
        delimiters = [",", "\n"]

        # Check for custom delimiters
        if numbers.startswith("//"):
            # Example: //[delim1][delim2]\n...
            # We'll split once at newline, parse everything in the first line after '//'
            header, numbers = numbers.split("\n", 1)
            # header might be "//[***][%%]" for example
            # find all bracketed delimiters
            bracketed = re.findall(r"\[(.*?)\]", header)  # captures anything inside [...]
            if bracketed:
                # we have one or more bracketed delimiters
                delimiters = list(bracketed)  # e.g. ["***", "%%"]
            else:
                # single char delimiter fallback
                delimiter = header[2]  # e.g. ;
                delimiters = [delimiter]

            # keep comma and newline in the pattern
            delimiters.append("\n")
            delimiters.append(",")

        # Build a regex pattern
        delimiters_escaped = [re.escape(d) for d in delimiters]
        pattern = "|".join(delimiters_escaped)
        parts = re.split(pattern, numbers)

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
            raise Exception(f"Negatives not allowed: " + ",".join(map(str, negatives)))
        return total
