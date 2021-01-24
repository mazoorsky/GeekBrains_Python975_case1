class Auto:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print('Машина едет')

    def car_stop(self):
        print('Машина стоит')

    def turn(self, direction):
        return f"Машина повернула " + direction

    def speed_control(self):
        print(f"Скорость автомобиля {self.name}: {self.speed} км/ч")

class WorkCar(Auto):

    def speed_control(self):
        if self.speed > 60:
            return f"Скорость {self.name} : {self.speed} км/ч. Превышение!"
        else:
            return f"Скорость {self.name} : {self.speed} км/ч"

class TownCar(Auto):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class SportCar(Auto):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class PoliceCar(Auto):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


volvo = TownCar(50, 'Blue', 'Volvo')
ferrari = SportCar(250, 'Red', 'Ferrari')
police = PoliceCar(120, 'White', 'Volkswagen')
work = WorkCar(80, 'yellow', 'honda')
print(work.speed_control())
print(ferrari.name, ferrari.turn('налево'))
print(f"Название: {volvo.name}, Цвет: {volvo.color}, Скорость: {volvo.speed}")
