# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        r = max(r, body.R)  # обработка аномалий при прохождении одного тела сквозь другое

        # Fx = (Gm1m2/r**2) * (delta_x/r)
        # Fy = (Gm1m2 / r ** 2) * (delta_y / r)
        force_coefficient = gravitational_constant * body.m * obj.m / r ** 3
        body.Fx += force_coefficient * (obj.x - body.x)
        body.Fy += force_coefficient * (obj.y - body.y)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    # Ускорение
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    # dr = v*dt + a*dt^2/2
    body.x += body.Vx * dt + ax * (dt ** 2) / 2
    body.y += body.Vy * dt + ay * (dt ** 2) / 2

    # dv = a*dt
    body.Vx += ax * dt
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
