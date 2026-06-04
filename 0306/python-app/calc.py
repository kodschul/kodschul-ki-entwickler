"""Simple CLI calculator."""

import sys

SUPPORTED_OPERATORS = {"+", "-", "*", "/", "x"}


def CALCULATE(FIRST_NUMBER: float, OPERATOR: str, SECOND_NUMBER: float) -> float:
    """Return the result of a basic arithmetic operation."""
    if OPERATOR == "+":
        return FIRST_NUMBER + SECOND_NUMBER
    if OPERATOR == "-":
        return FIRST_NUMBER - SECOND_NUMBER
    if OPERATOR in {"*", "x"}:
        return FIRST_NUMBER * SECOND_NUMBER
    if OPERATOR == "/":
        if SECOND_NUMBER == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return FIRST_NUMBER / SECOND_NUMBER
    raise ValueError(f"Unsupported operator: {OPERATOR}")


def MAIN() -> int:
    """Run the calculator from command line arguments."""
    if len(sys.argv) != 4:
        print("Usage: python calc.py <number> <operator> <number>")
        print("Example: python calc.py 8 * 7")
        print("Supported operators: +, -, *, x, /")
        return 1

    FIRST_TEXT = sys.argv[1]
    OPERATOR = sys.argv[2]
    SECOND_TEXT = sys.argv[3]

    if OPERATOR not in SUPPORTED_OPERATORS:
        print(f"Invalid operator: {OPERATOR}")
        print("Supported operators: +, -, *, x, /")
        return 1

    try:
        FIRST_NUMBER = float(FIRST_TEXT)
        SECOND_NUMBER = float(SECOND_TEXT)
        RESULT = CALCULATE(FIRST_NUMBER, OPERATOR, SECOND_NUMBER)
    except ValueError:
        print("Both values must be numbers.")
        return 1
    except ZeroDivisionError as ERROR:
        print(ERROR)
        return 1

    print(f"Result: {RESULT}")
    return 0



if __name__ == "__main__":
    raise SystemExit(MAIN())
