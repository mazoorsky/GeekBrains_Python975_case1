class Road:
    _length = 0
    _width = 0
    weight = 0
    height = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        self.weight = 25
        self.height = 5
        mass = (self._length * self._width * self.weight * self.height) / 1000
        return mass


asph = Road(5000, 20)
print('Тонн асфальта надо: ', asph.calc())
