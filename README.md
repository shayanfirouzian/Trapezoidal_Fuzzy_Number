# Trapezoidal_Fuzzy_Number
A library to work with trapezoidal fuzzy numbers
Suppose that we want to create A and B, which are Trapezoidal Fuzzy Numbers:
```
from Trapezoidal_Fuzzy_Number import TrapezoidalFuzzyNumber
A = TrapezoidalFuzzyNumber([1, 2, 3, 4])
B = TrapezoidalFuzzyNumber([2, 3, 4, 5])
```

# Addition
result_add = A + B
print(result_add)  # Output as a list

# Subtraction
result_sub = A - B
print(result_sub)  # Output as a list

# Multiplication
result_mul = A * B
print(result_mul)  # Output as a list

# Multiplication by a scalar
scalar = 2.5
result_scalar_mul = scalar * A
print(result_scalar_mul)  # Output as a list

# Division
result_div = A / B
print(result_div)  # Output as a list

# Division by a scalar
result_scalar_div = A // 3
