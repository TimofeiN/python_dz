from abc import abstractmethod


class Square:
    def __init__(self, cells, line=0):
        self.cells = cells
        self.line = line

    def __str__(self):
        return f'клетка с {self.cells} ячеек'

    def __add__(self, other):
        return Square(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Square(self.cells - other.cells)
        else:
            print(f'Невозможно вычесть разница меньше 0')

    def __mul__(self, other):
        return Square(self.cells * other.cells)

    def __floordiv__(self, other):
        return Square(self.cells // other.cells)

    def __truediv__(self, other):
        return Square(self.cells / other.cells)

    @abstractmethod
    def make_order(self, cells, line):
        x = cells // line
        y = cells % line
        output = (f'*' * line + f"\\n") * x + f'*' * y
        return output


sc1 = Square(40)
sc2 = Square(30)

a = sc1 + sc2
print(a)
print(sc1.make_order(12, 5))
