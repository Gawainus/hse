from turtle import *
from random import randrange
from freegames import square, vector

level = 1
picked_level = 1

heli = vector(-130, 0)

ob = [vector(190, 0)]
aim = vector(-50, 0)
place = vector(0, -10)


def pick_lvl():
    print("Please enter a level between 1 to 3")
    c = input()
    if c.isdigit():
        lvl = int(c)
        if 0 < lvl < 4:
            return lvl

    return pick_lvl()


def lvl_coeff():
    """
    Get a coefficient based on initially picked level. The higher the level,
    the more sensitive the chopper's movements.
    :return:
    """
    return 0.5 * (1 + picked_level)


def boost(dy):
    """
    boost up the chopper
    :param dy: positive int
    :return: None
    """
    heli.y += dy * lvl_coeff()


def hori(dx):
    """
    change chopper horizontally
    :param dx: int
    :return:
    """
    heli.x += dx * lvl_coeff()


def inside(heli):
    """
    Check if the chopper is still inside the walls.
    :param heli: the chopper's dot
    :return:
    """
    return -200 < heli.x < 190 and -200 < heli.y < 190


def collide(heli):
    print("heli", heli.x, heli.y)
    for o in ob:
        print("o", o.x, o.y)
        if abs(heli.x - o.x) < 10 and heli.y == o.y:
            return True

    return False


def get_ob_speed():
    """
    Generate the speed of blocks based on initially picked level
    :return:
    """
    return randrange(10, 30, 10) * lvl_coeff()


def move():
    """
    Main event loop
    :return:
    """
    global level
    if not inside(heli) or collide(heli):
        square(heli.x, heli.y, 9, 'red')
        update()
        print("Game Over!")
        return

    if len(ob) < level:
        tail = ob[-1].copy()
        tail.move(place)
        ob.append(tail)

    clear()

    # Generate new frame
    lu = False
    if ob[0].x < -210:
        level += 1
        lu = True
        start_y = randrange(-110, 210, 10)
        print("You have reached lvl:", level)

    s = get_ob_speed()
    for i, o in enumerate(ob):
        if lu:
            o.x += 420
            o.y = start_y + (i * -10)

        o.x -= s
        square(o.x, o.y, 9, 'brown')

    heli.y -= 5
    square(heli.x, heli.y, 9, 'black')
    update()
    ontimer(move, 100)


picked_level = pick_lvl()
level = picked_level

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: boost(30), 'space')
onkey(lambda: hori(-10), 'Left')
onkey(lambda: hori(10), 'Right')
move()
done()

