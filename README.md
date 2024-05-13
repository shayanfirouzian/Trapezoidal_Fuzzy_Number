# Trapezoidal Fuzzy Number
A library to work with trapezoidal fuzzy numbers in Python\
First, you need to install the package:
```ruby
pip install Trapezoidal-Fuzzy-Number
```
When done, you can import it:
```ruby
from Trapezoidal_Fuzzy_Number import TrapezoidalFuzzyNumber
```
Suppose that we want to create A and B, which are Trapezoidal Fuzzy Numbers:
```ruby
A = TrapezoidalFuzzyNumber([1, 2, 3, 4])
B = TrapezoidalFuzzyNumber([2, 3, 4, 5])
```

# Addition of two Trapezoidal Fuzzy Numbers
```ruby
result_add = A + B
print(result_add)
```

# Subtraction of two Trapezoidal Fuzzy Numbers
```ruby
result_sub = A - B
print(result_sub)
```

# Multiplication of two Trapezoidal Fuzzy Numbers
```ruby
result_mul = A * B
print(result_mul)
```

# Division of two Trapezoidal Fuzzy Numbers
```ruby
result_div = A / B
print(result_div)
```

# Multiplication of a Trapezoidal Fuzzy Number by a Real Number
```ruby
result_real_by_fuzzy_mul = 2.5 * A
print(result_real_by_fuzzy_mul)
```

# Division  of a Trapezoidal Fuzzy Number by a Real Number
```ruby
result_fuzzy_by_real_div = A // 3
print(result_fuzzy_by_real_div)
```

# Division of a Real Number by a Trapezoidal Fuzzy Number
```ruby
result_real_by_fuzzy_div = 2.5 / A
print(result_real_by_fuzzy_div)
```
