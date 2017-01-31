import numpy as np
from core.soft import bezier
from numpy import sin, cos
from core.anim import Animation
from core.obj import Vector, Line, Curve

sHandSpeed = 12
mHandSpeed = sHandSpeed/60
hHandSpeed = mHandSpeed/12

b = bezier([0, 0, 0, 1, 1, 1, 1, 1])

def update_s(s, t, tmax):
    t *= -sHandSpeed * 2*np.pi
    t += np.pi/2
    s.p2 = (cos(t)/2, sin(t)/2)

def update_m(v, t, tmax):
    t *= -mHandSpeed * 2*np.pi
    t += np.pi/2
    v.head = (cos(t)/3, sin(t)/3)

def update_h(v, t, tmax):
    t *= -hHandSpeed * 2*np.pi
    t += np.pi/2
    v.head = (cos(t)/5, sin(t)/5)

def update_c(c, t, tmax):
    c.tmax = t/tmax

def init(anim):
    h = anim.create(
        Vector,
        0, 1/5,
        color='.50',
        update=update_h
    )
    anim.create(
        Vector,
        0, 1/3,
        color='w',
        update=update_m
    )
    anim.create(
        Line,
        0, 0, 0, 1/2,
        color='r',
        lw=1,
        update=update_s
    )
    anim.create(
        Curve,
        lambda t: (2*t-1, 2*b(t)-1),
        color='g',
        update=update_c
    )

if __name__ == '__main__':
    global an
    an = Animation(
        dt=0.0001,
        length=1/mHandSpeed,
        speed=10,
        init_func=init,
        repeat=False,
        softener=b
    ).play()
