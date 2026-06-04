import pytest

from calc import CALCULATE, MAIN


def test_calculate_addition():
    # Happy Path: Addition
    assert CALCULATE(2.0, "+", 3.0) == 5.0


def test_calculate_subtraction():
    # Happy Path: Subtraktion
    assert CALCULATE(10.0, "-", 4.0) == 6.0


def test_calculate_multiplication_star():
    # Happy Path: Multiplikation mit *
    assert CALCULATE(6.0, "*", 7.0) == 42.0


def test_calculate_multiplication_x():
    # Happy Path: Multiplikation mit x
    assert CALCULATE(6.0, "x", 7.0) == 42.0


def test_calculate_division():
    # Happy Path: Division
    assert CALCULATE(8.0, "/", 2.0) == 4.0


def test_calculate_division_by_zero_raises():
    # Ungültiger Wert: Division durch 0
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        CALCULATE(8.0, "/", 0.0)


def test_calculate_unsupported_operator_raises():
    # Ungültiger Wert: nicht unterstützter Operator
    with pytest.raises(ValueError, match="Unsupported operator"):
        CALCULATE(1.0, "^", 2.0)


def test_main_with_wrong_argument_count(monkeypatch, capsys):
    # Leere Eingabe/zu wenig Eingaben
    monkeypatch.setattr("calc.sys.argv", ["calc.py"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 1
    assert "Usage: python calc.py <number> <operator> <number>" in captured.out
    assert "Supported operators: +, -, *, x, /" in captured.out


def test_main_with_invalid_operator(monkeypatch, capsys):
    # Ungültiger Wert: Operator
    monkeypatch.setattr("calc.sys.argv", ["calc.py", "2", "^", "3"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 1
    assert "Invalid operator: ^" in captured.out
    assert "Supported operators: +, -, *, x, /" in captured.out


def test_main_with_non_numeric_values(monkeypatch, capsys):
    # Ungültiger Wert: keine Zahlen
    monkeypatch.setattr("calc.sys.argv", ["calc.py", "abc", "+", "3"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 1
    assert "Both values must be numbers." in captured.out


def test_main_with_division_by_zero(monkeypatch, capsys):
    # Ungültiger Wert: Division durch 0
    monkeypatch.setattr("calc.sys.argv", ["calc.py", "5", "/", "0"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 1
    assert "Cannot divide by zero." in captured.out


def test_main_success(monkeypatch, capsys):
    # Happy Path: gültige CLI-Eingabe
    monkeypatch.setattr("calc.sys.argv", ["calc.py", "8", "*", "7"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 0
    assert "Result: 56.0" in captured.out


def test_all_functions_in_one_case(monkeypatch, capsys):
    # Ein gemeinsamer Testfall für alle Funktionen (CALCULATE + MAIN)
    assert CALCULATE(1.0, "+", 2.0) == 3.0
    assert CALCULATE(5.0, "-", 3.0) == 2.0
    assert CALCULATE(4.0, "*", 2.0) == 8.0
    assert CALCULATE(4.0, "x", 2.0) == 8.0
    assert CALCULATE(9.0, "/", 3.0) == 3.0

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        CALCULATE(1.0, "/", 0.0)

    with pytest.raises(ValueError, match="Unsupported operator"):
        CALCULATE(1.0, "%", 1.0)

    monkeypatch.setattr("calc.sys.argv", ["calc.py", "7", "+", "8"])
    return_code = MAIN()
    captured = capsys.readouterr()

    assert return_code == 0
    assert "Result: 15.0" in captured.out
