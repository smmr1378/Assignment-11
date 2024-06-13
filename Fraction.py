class Fraction:
    def __init__(self, ss, mm):
        # properties
        self.s = ss
        self.m = mm

    # method
    def sum(self, k2):
        s = self.s * k2.m + self.m * k2.s
        m = self.m *k2.m
        x = Fraction(s, m)
        return x

    def mul(self, kasr_1):
        result_s = kasr_1.s * self.s
        result_m = kasr_1.m * self.m
        x = Fraction(result_s, result_m)
        return x

    def sub(self, other):
        new_numerator = self.s * other.m - self.m * other.s
        new_denominator = self.m * other.s
        x = Fraction(new_denominator, new_denominator)
        return x

    def div(self, kasr_2):
        result_s = kasr_2.s * self.m
        result_m = kasr_2.m * self.s
        x = Fraction(result_s, result_m)
        return x

    def fraction_to_number(self):
        x = self.s / self.m
        return x

    def show(self):
        print (self.s, "/", self.m)

a = Fraction(2, 3)
a.show()

b = Fraction(7, 1)
b.show()

z = b.mul(a)
z.show()

w = a.sum(b)
w.show()