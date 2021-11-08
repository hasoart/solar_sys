# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, object_dict):
        '''
        получает на вход словарь, содержащий характеристики объекта:
        m - масса звезды
        x, y - ее координаты
        R - радиус звезды
        color - цвет звезды
        Vx, Vy - скорости вдоль координат
        Fx, Fy - силы вдоль координат
        '''
        self.type = object_dict["type"]
        self.m = object_dict["m"]
        self.x = object_dict["x"]
        self.y = object_dict["y"]
        self.R = object_dict["R"]
        self.color = object_dict["color"]
        self.Vx = object_dict["Vx"]
        self.Vy = object_dict["Vy"]
        self.Fx = 0
        self.Fy = 0



class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, object_dict):
        '''
        получает на вход словарь, содержащий характеристики объекта:
        m - масса планеты
        x, y - ее координаты
        R - радиус планеты
        color - цвет планеты
        Vx, Vy - скорости вдоль координат
        Fx, Fy - силы вдоль координат
        '''
        self.type = object_dict["type"]
        self.m = object_dict["m"]
        self.x = object_dict["x"]
        self.y = object_dict["y"]
        self.R = object_dict["R"]
        self.color = object_dict["color"]
        self.Vx = object_dict["Vx"]
        self.Vy = object_dict["Vy"]
        self.Fx = 0
        self.Fy = 0
