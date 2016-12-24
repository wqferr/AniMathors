import numpy as np
import colorsys
from numpy import sin, cos
from core.anim import Animation
from core.obj import Point, Line, Vector, Curve

def update_p1(p1, t, dt):
    p1.x = np.cos(t)

def update_p2(p2, t, dt):
    p2.y = np.sin(t/3)

def update_p3(p3, t, dt):
    p3.pos = (p1.x, p2.y)
    c = colorsys.rgb_to_hsv(*p3.color)
    c = ((c[0]+dt/(2*np.pi)) % 1, c[1], c[2])
    p3.color = colorsys.hsv_to_rgb(*c)

def update_line(l, t, dt):
    l.p1 = (np.cos(t)/2, np.sin(t)/2)
    l.p2 = (-np.cos(t)/2, -np.sin(t)/2)

def update_v(v, t, dt):
    r2 = np.sqrt(2)/4
    c = r2 * cos(2*t)
    s = r2/3 * sin(2*t)

    v.hx = s - c
    v.hy = c + s

def update_c(c, t, dt):
    c.update_params(
        tmin=min(v.hx, p3.x),
        tmax=max(v.hx, p3.x),
        dt=max(abs(p3.y)/5, 0.001)
    )

def init(anim):
    global p1, p2, p3, v
    p1 = anim.add(
        Point,
        0, 0,
        color='g', size=10,
        update=update_p1
    )
    p2 = anim.add(
        Point,
        0, 0,
        color='b', size=10,
        update=update_p2
    )
    p3 = anim.add(
        Point,
        0, 0,
        color='r', size=7,
        update=update_p3
    )
    anim.add(
        Line,
        0, 0, 0, 0,
        color='r',
        update=update_line
    )
    v = anim.add(
        Vector,
        -.05, -.25,
        color='b',
        update=update_v
    )
    c = anim.add(
        Curve,
        lambda t: t**3,
        -1, 1,
        color='w',
        update=update_c
    )

if __name__ == '__main__':
    Animation(dt=0.01, tmax=6*np.pi, init_func=init, repeat=True).play()
