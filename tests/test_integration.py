import pytest
from cli import calculate
from calculator import Calculator

def test_full_user_interaction_addition():
    # Simulate: enter 5, press +, enter 3, press =
    result = calculate(5, "+", 3)
    assert result == 8

def test_clear_after_calculation_resets_to_zero():
    calc = Calculator()
    _ = calc.add(9, 1)
    assert calc.clear() == 0