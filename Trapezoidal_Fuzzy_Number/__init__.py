class TrapezoidalFuzzyNumber:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def membership(self, x):
        if x < self.a:
            return 0
        elif self.a <= x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b <= x < self.c:
            return 1
        elif self.c <= x < self.d:
            return (self.d - x) / (self.d - self.c)
        else:
            return 0

    def __add__(self, other):
        # Pointwise addition of membership functions
        return TrapezoidalFuzzyNumber(
            max(self.a, other.a),
            max(self.b, other.b),
            min(self.c, other.c),
            min(self.d, other.d)
        )

    def __mul__(self, other):
        # Pointwise multiplication of membership functions
        return TrapezoidalFuzzyNumber(
            max(self.a * other.a, self.a * other.b, self.b * other.a, self.b * other.b),
            max(self.a * other.c, self.b * other.c, self.c * other.a, self.c * other.b),
            min(self.b * other.c, self.c * other.c, self.c * other.d, self.d * other.c),
            min(self.c * other.d, self.d * other.d, self.d * other.d, self.d * other.d)
        )

    def __truediv__(self, other):
        # Pointwise division of membership functions
        return TrapezoidalFuzzyNumber(
            max(self.a / other.a, self.a / other.b, self.b / other.a, self.b / other.b),
            max(self.a / other.c, self.b / other.c, self.c / other.a, self.c / other.b),
            min(self.b / other.c, self.c / other.c, self.c / other.d, self.d / other.c),
            min(self.c / other.d, self.d / other.d, self.d / other.d, self.d / other.d)
        )

    def multiply_by_real(self, r):
        # Multiply by a real number
        return TrapezoidalFuzzyNumber(
            r * self.a,
            r * self.b,
            r * self.c,
            r * self.d
        )

    def divide_by_real(self, r):
        # Divide by a real number
        return TrapezoidalFuzzyNumber(
            self.a / r,
            self.b / r,
            self.c / r,
            self.d / r
        )