def lazy_evaluation(function):
    evaluated = False
    value = None

    def wrapper():
        nonlocal evaluated, value
        if not evaluated:
            value = function()
            evaluated = True
        return value

    return wrapper

# Example usage
def expensive_calculation():
    print("Performing expensive calculation...")
    return 42

lazy_calculation = lazy_evaluation(expensive_calculation)

# The expensive calculation is not performed until we actually access the value
print("Accessing value...")
print(lazy_calculation())  # This triggers the evaluation
print("Accessing value again...")
print(lazy_calculation())  # The value has already been evaluated, so the expensive calculation is not performed again
