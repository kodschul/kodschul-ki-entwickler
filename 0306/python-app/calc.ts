type calculator_operator = "+" | "-" | "*" | "/";

export function add_numbers(a: number, b: number): number {
  return a + b;
}

export function subtract_numbers(a: number, b: number): number {
  return a - b;
}

export function multiply_numbers(a: number, b: number): number {
  return a * b;
}

export function divide_numbers(a: number, b: number): number {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }

  return a / b;
}

export function calculate_result(
  a: number,
  b: number,
  operator: calculator_operator,
): number {
  if (operator === "+") {
    return add_numbers(a, b);
  }

  if (operator === "-") {
    return subtract_numbers(a, b);
  }

  if (operator === "*") {
    return multiply_numbers(a, b);
  }

  return divide_numbers(a, b);
}
