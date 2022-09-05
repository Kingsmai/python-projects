# Warm or Cold (E)
# Define a function that:
# (1) takes a temperature as parameter
# (2) returns Warm if the temperature is greater than 7
# (3) returns Cold if the temperature is equal or less than 7
# If I called you function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold in both cases, and so on.

def foo(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"