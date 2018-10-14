
class Polinom:
    def __init__(self, a = 0, b = 0, c = 0, d = 0, xi = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xi = xi

    def calculate(self, value):
        return self.a + self.b * (value - self.xi) + self.c(value - self.xi)**2 + self.d * (value - self.xi)**3

    def __str__(self):
        if self.a == 0:
              return(str(round(self.b, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')' + \
                       "{0:+}".format(round(self.c, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^2' + \
                       "{0:+}".format(round(self.d, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^3 ;')
        if self.b == 0:
              return(str(round(self.a, 2))  + "{0:+}".format(round(self.c, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^2 +' +\
                       "{0:+}".format(round(self.d, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^3 ;')
        if self.c == 0:
              return(str(round(self.a, 2)) + "{0:+}".format(round(self.b, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')' + \
                       "{0:+}".format(round(self.d, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^3 ;')
        if self.d == 0:
              return(str(round(self.a, 2)) + "{0:+}".format(round(self.b, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')' + \
                       "{0:+}".format(round(self.c, 2)) + '(x' +  "{0:+}".format(round(self.xi, 2)) + ')^2 ;')
        if self.xi == 0:
              return(str(round(self.a, 3)) + "{0:+}".format(round(self.b, 3)) + 'x' + "{0:+}".format(round(self.c, 3)) + 'x' +\
                       '^2 ' + "{0:+}".format(round(self.d, 3)) + 'x' + '^3 ;')  
        else:
              return(str(round(self.a, 3)) + "{0:+}".format(round(self.b, 3)) + '(x' + "{0:+}".format(round(self.xi, 3)) + \
                       ')' + "{0:+}".format(round(self.c, 3)) + '(x' + "{0:+}".format(round(self.xi, 3)) +\
                       ')^2 ' + "{0:+}".format(round(self.d, 3)) + '(x' + "{0:+}".format(round(self.xi, 3)) + ')^3 ;')  