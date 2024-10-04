def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform the division
        result = num / denom
        return f"The result of the division is {result:.1f}"  # Format to one decimal place

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

