import numpy as np
from core.anim import Animation
from core.obj import Point, Line

def update_p1(p1, t):
    p1.x = np.cos(t)

def update_p2(p2, t):
    p2.y = np.sin(3*t)

def update_p3(p3, t):
    p3.pos = (p1.x, p2.y)

def update_line(l, t):
    l.pos1 = (np.cos(t)/2, np.sin(t)/2)
    l.pos2 = (-np.cos(t)/2, -np.sin(t)/2)

p1, p2 = None, None
def init(anim):
    global p1, p2
    p1 = anim.add(
        Point,
        color='g', size=10,
        update=update_p1
    )
    p2 = anim.add(
        Point,
        color='b', size=10,
        update=update_p2
    )
    anim.add(
        Point,
        color='w', size=5,
        update=update_p3
    )
    anim.add(
        Line,
        color='r',
        update=update_line
    )

if __name__ == '__main__':
    anim = Animation(dt=0.01*np.pi, init_func=init)
    anim.play(interval=100/6, frames=200)
