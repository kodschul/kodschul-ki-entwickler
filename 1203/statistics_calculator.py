"""
statistics_calculator.py

A practical demonstration of clean Python code:
  - Type hints for all parameters and return values
  - A descriptive docstring with argument/return documentation
  - Input validation with clear error messages
  - A named return type (dataclass) instead of a raw dict
  - Pure functions with no side effects
"""

from dataclasses import dataclass
from collections import Counter
from typing import Optional


@dataclass
class Stats:
    """Container for the three classic descriptive statistics."""
    mean: float
    median: float
    mode: Optional[float]   # None when every value appears exactly once


def calculate_statistics(numbers: list[float]) -> Stats:
    """
    Compute the mean, median, and mode for a list of numbers.

    Args:
        numbers: A non-empty list of numeric values (int or float).

    Returns:
        A Stats dataclass with mean, median, and mode fields.
        mode is None when no value appears more than once.

    Raises:
        TypeError:  If `numbers` is not a list.
        ValueError: If `numbers` is empty.

    Examples:
        >>> stats = calculate_statistics([1, 2, 2, 3, 4])
        >>> stats.mean
        2.4
        >>> stats.median
        2
        >>> stats.mode
        2
    """
    # --- Input validation -------------------------------------------------
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list, got {type(numbers).__name__!r}.")

    if len(numbers) == 0:
        raise ValueError("The list must contain at least one number.")

    # --- Mean -------------------------------------------------------------
    # Sum all values and divide by the count (avoids importing statistics).
    mean = sum(numbers) / len(numbers)

    # --- Median -----------------------------------------------------------
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2

    if len(sorted_nums) % 2 == 0:
        # Even count: average the two middle elements
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # Odd count: take the single middle element
        median = sorted_nums[mid]

    # --- Mode -------------------------------------------------------------
    # Counter.most_common(1) returns [(value, count)] for the top element.
    frequency = Counter(numbers)
    top_value, top_count = frequency.most_common(1)[0]

    # A meaningful mode only exists when at least one value repeats.
    mode = top_value if top_count > 1 else None

    return Stats(mean=mean, median=median, mode=mode)


# ---------------------------------------------------------------------------
# Quick demo — runs only when the script is executed directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sample_data = [4, 1, 2, 2, 3, 5, 2, 8]

    result = calculate_statistics(sample_data)

    print(f"Data   : {sample_data}")
    print(f"Mean   : {result.mean:.2f}")
    print(f"Median : {result.median}")
    print(f"Mode   : {result.mode if result.mode is not None else 'No mode (all values unique)'}")
