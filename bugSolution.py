def function_with_uncommon_error_fixed(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("Both operands cannot be zero.")
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

try:
    result = function_with_uncommon_error_fixed(0, 0)
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # This will now raise the appropriate exception.