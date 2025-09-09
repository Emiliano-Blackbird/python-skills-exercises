class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


rec1 = Rectangulo(5, 10)

print(f"Area: {rec1.area()}")
print(f"Perímetro: {rec1.perimetro()}")
