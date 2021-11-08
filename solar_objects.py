# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, m, x, y, R, color, Vx, Vy):
        '''
        m - масса звезды
        x, y - ее координаты
        R - радиус звезды
        color - цвет звезды
        Vx, Vy - скорости вдоль координат
        Fx, Fy - силы вдоль координат
        '''
        self.type = "Star"
        self.m = m
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = 0
        self.Fy = 0



class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, m, x, y, R, color, Vx, Vy):
        '''
        m - масса планеты
        x, y - ее координаты
        R - радиус планеты
        color - цвет планеты
        Vx, Vy - скорости вдоль координат
        Fx, Fy - силы вдоль координат
        '''
        self.type = "Planet"
        self.m = m
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = 0
        self.Fy = 0
