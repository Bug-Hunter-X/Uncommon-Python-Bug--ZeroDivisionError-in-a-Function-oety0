def function_with_error_handling(a, b):
    if a == 0:
        return "Division by zero is not allowed."  # Handle the error gracefully
    return a + b

# Test the function
print(function_with_error_handling(5, 3))
print(function_with_error_handling(0, 3))