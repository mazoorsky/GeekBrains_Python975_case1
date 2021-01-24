class Stationery:
    title = 'Title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):

    def draw(self):
        print('Рисуем маркером')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
