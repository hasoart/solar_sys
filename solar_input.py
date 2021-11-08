# coding: utf-8
# license: GPLv3

import json

from solar_objects import Star, Planet
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """
    objects = []
    with open(input_filename, 'r') as input_file:
        objects_list = json.load(input_file)['objects']

        for obj in objects_list:
            if obj['type'] == 'Star':
                objects.append(Star(obj))
            elif obj['type'] == 'Planet':
                objects.append(Planet(obj))
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def write_space_objects_data_to_file(output_filename, space_objects):
    # TODO
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME!


if __name__ == "__main__":
    print("This module is not for direct call!")
