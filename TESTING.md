# Testing Strategy

This project implements a testing strategy for the Quick-Calc calculator application using both **unit tests** and **integration tests**.

## What was tested

The following components were tested:

- Core calculator operations (addition, subtraction, multiplication, division)
- Edge cases such as division by zero
- Handling of negative numbers and decimal numbers
- Interaction between the input layer (cli.py) and the calculation logic (calculator.py)

## What was not tested

The following aspects were intentionally not tested because they are outside the scope of this assignment:

- Performance testing
- Security testing
- Graphical user interface behavior

The assignment focuses mainly on functional correctness and testing concepts.

---

# Testing Pyramid

The testing approach follows the **Testing Pyramid** concept.

Most tests are **unit tests**, which verify individual functions in isolation. These tests are fast and provide immediate feedback when changes are made.

A smaller number of **integration tests** ensure that different parts of the system work correctly together, such as the interaction between the CLI layer and the calculator logic.

---

# Black-box vs White-box Testing

Two testing approaches were used:

**White-box testing** was used in unit tests because internal functions of the calculator are tested directly.

**Black-box testing** was used in integration tests because the system is tested through its external interface without relying on internal implementation details.

---

# Functional vs Non-Functional Testing

This project focuses mainly on **functional testing**, ensuring that the calculator returns correct results for each mathematical operation.

Non-functional testing such as performance or scalability testing was not implemented because it is not required for this assignment.

---

# Regression Testing

The test suite can be used as **regression tests**.  
Whenever new features are added or changes are made, running the full test suite ensures that existing functionality still works correctly.

---

# Test Results

| Test Name | Type | Result |
|-----------|------|-------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_full_user_interaction_addition | Integration | Pass |
| test_clear_after_calculation_resets_to_zero | Integration | Pass |