import math


def add(number_to_add, other_number_to_add):
    return number_to_add + other_number_to_add


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def multiply(first_factor, second_factor):
    return first_factor * second_factor


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return dividend / divisor


def modulo(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return dividend % divisor


def square_root(number):
    if number < 0:
        raise ValueError("Quadratwurzel aus negativer Zahl ist nicht erlaubt")
    return math.sqrt(number)


def main():
    binary_operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo,
    }

    print("Einfacher Taschenrechner (beenden mit 'q')")
    print("Beispiele: 3 + 4  |  10 % 3  |  sqrt 16")
    while True:
        user_input = input("Eingabe: ").strip()
        if user_input.lower() == "q":
            break

        input_parts = user_input.split()

        try:
            if len(input_parts) == 2 and input_parts[0].lower() == "sqrt":
                number = float(input_parts[1])
                result = square_root(number)
                print(f"Ergebnis: {result}")
                continue

            if len(input_parts) != 3 or input_parts[1] not in binary_operations:
                print("Ungueltige Eingabe. Format: <Zahl> <Operator> <Zahl> oder 'sqrt <Zahl>'")
                continue

            first_number = float(input_parts[0])
            operator_symbol = input_parts[1]
            second_number = float(input_parts[2])
            result = binary_operations[operator_symbol](first_number, second_number)
            print(f"Ergebnis: {result}")
        except ValueError as error:
            print(f"Fehler: {error}")


if __name__ == "__main__":
    main()
