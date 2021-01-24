import time


class TrafficLight:

    def __init__(self, color):
        self.color = color

    def running(self):
        i = 0
        while i < 3:
            self.color = 'red'
            print('Цвет светофора: ', self.color)
            time.sleep(7)
            self.color = 'yellow'
            print('Цвет светофора: ', self.color)
            time.sleep(2)
            self.color = 'green'
            print('Цвет светофора: ', self.color)
            time.sleep(10)
            i += 1


switch = TrafficLight(0)
switch.running()
