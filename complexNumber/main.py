class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def show(self):
        print(self.real, "+", self.imag, "i")

    def add(self, other):
        final = ComplexNumber()
        final.real = self.real + other.real
        final.imag = self.imag + other.imag
        return final

    def subtract(self, other):
        final = ComplexNumber()
        final.real = self.real - other.real
        final.imag = self.imag - other.imag
        return final

    def mult(self, other):
        final = ComplexNumber()
        final.real = ((self.real * other.real) - (self.imag * other.imag))
        final.imag = ((self.real * other.imag) + (self.imag * other.real))
        return final


a = ComplexNumber(2, 3)
b = ComplexNumber(4, 6)
c = a.add(b)
c.show()
d = a.subtract(b)
d.show()
e = a.mult(b)
e.show()
