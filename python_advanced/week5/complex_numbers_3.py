class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        """
        re: int, float
        im: int, float
        """
        if type(re) not in (int, float):
            raise TypeError

        if type(im) not in (int, float):
            raise TypeError

        self.re = re
        self.im = im

    def __str__(self) -> str:
        return str(f"{self.re}{self.im:+}i")

    # Part 2
    def __add__(self, other):
        """
        other: int, float, Complex
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)

        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)

        raise TypeError

    def __sub__(self, other):
        """
        other: int, float, Complex
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re - other, self.im)

        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)

        raise TypeError

    # Part 3
    def __mul__(self, other):
        """
        other: int, float, Complex
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re * other, self.im * other)

        if isinstance(other, Complex):
            return Complex(
                self.re * other.re - self.im * other.im,
                self.re * other.im + self.im * other.re)

        raise TypeError

    def __truediv__(self, other):
        """
        other: int, float, Complex
        """
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ZeroDivisionError

            return Complex(self.re / float(other), self.im / float(other))

        denom = float(other.re ** 2 + other.im ** 2)
        return self * Complex(other.re/denom, -other.im/denom)


c = Complex(-1, 2)
c2 = Complex(3, -7)
print(c * c2)
print(c * 3)
print(c * 0)
print(c / c2)
print(c / 0.3)
print(Complex(-5) * Complex(5.1, 5.8))
# print(c / 0)
