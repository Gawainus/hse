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
