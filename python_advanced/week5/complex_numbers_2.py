
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



c = Complex(1, 2)
c2 = Complex(-0.5, -2)

print(c - 1)
print(c - 0.5)
print(c - c2)

c = Complex(1, -2)
c2 = Complex(3, -7)
print(c * c2)
print(c / c2)
