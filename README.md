# Uncommon Division by Zero Bug in Python

This repository demonstrates an uncommon error related to division by zero in Python.  The function `function_with_uncommon_error` handles the cases where either `a` or `b` is zero, but it does not explicitly handle the case where *both* are zero. This leads to unexpected behavior (returning 0) rather than raising a `ZeroDivisionError`.

The `bug.py` file shows the problematic code, and the `bugSolution.py` file demonstrates a corrected version that handles all possible scenarios, including both operands being zero.

This bug highlights the importance of thoroughly testing edge cases and ensuring appropriate exception handling in your code.