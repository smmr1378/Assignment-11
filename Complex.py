class Complex:
    
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)

    def show(self):
        sign = '+' if self.image >= 0 else '-'
        image = abs(self.image)
        print(f"{self.real} {sign} i{image}")

# نمونه استفاده
num1 = Complex(5, 3)
num2 = Complex(2, 4)
result_sum = num1 + num2
result_sub = num1 - num2

result_sum.show()  # نمایش: 7 + i7
result_sub.show()  # نمایش: 3 - i1