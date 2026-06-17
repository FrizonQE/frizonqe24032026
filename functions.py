def calculate(a: float = 0, b: float = 0, operation: str = "sum") -> float:
    if operation == "sub":
        return a - b
    return a + b


def change_text(text: str = "", upper: bool = True) -> str:
    if upper:
        return text.upper()
    return text.lower()


def sum_numbers(numbers: str = "1,2,3", separator: str = ",") -> int:
    parts = numbers.split(separator)

    total = 0
    for part in parts:
        total += int(part)

    return total