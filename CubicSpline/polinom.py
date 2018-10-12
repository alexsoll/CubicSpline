
class Polinom:
    def __init__(self, a = 0, b = 0, c = 0, d = 0, xi = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xi = xi

    def calculate(self, value):
        return self.a + self.b * (value - self.xi) + self.c(value - self.xi)**2 + self.d * (value - self.xi)**3