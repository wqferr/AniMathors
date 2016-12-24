import numpy as np
import colorsys
from numpy import sin, cos
from core.anim import Animation
from core.obj import Point, Line, Vector

def update_p1(p1, t, dt):
    p1.x = np.cos(t)

def update_p2(p2, t, dt):
    p2.y = np.sin(3*t)

def update_p3(p3, t, dt):
    p3.pos = (p1.x, p2.y)
    c = colorsys.rgb_to_hsv(*p3.color)
    c = ((c[0]+dt/(2*np.pi)) % 1, c[1], c[2])
    p3.color = colorsys.hsv_to_rgb(*c)

def update_line(l, t, dt):
    l.pos1 = (np.cos(t)/2, np.sin(t)/2)
    l.pos2 = (-np.cos(t)/2, -np.sin(t)/2)

def update_v(v, t, dt):
    r2 = np.sqrt(2)/4
    c = r2 * cos(2*t)
    s = r2/3 * sin(2*t)

    v.hx = c - s
    v.hy = c + s

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
        color='r', size=7,
        update=update_p3
    )
    anim.add(
        Line,
        color='r',
        update=update_line
    )
    v = anim.add(
        Vector,
        -.05, -.25,
        color='b',
        update=update_v
    )

if __name__ == '__main__':
    anim = Animation(dt=0.005*np.pi, init_func=init)
    anim.play(interval=100/6, frames=2000)
