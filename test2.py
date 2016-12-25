import numpy as np
import core.softening as s
from numpy import sin, cos
from core.anim import Animation
from core.obj import Vector, Line

sHandSpeed = 12
mHandSpeed = sHandSpeed/60
hHandSpeed = mHandSpeed/12


def update_s(s, t, dt):
    t *= -sHandSpeed * 2*np.pi
    t += np.pi/2
    s.p2 = (cos(t)/2, sin(t)/2)

def update_m(v, t, dt):
    t *= -mHandSpeed * 2*np.pi
    t += np.pi/2
    v.head = (cos(t)/3, sin(t)/3)

def update_h(v, t, dt):
    t *= -hHandSpeed * 2*np.pi
    t += np.pi/2
    v.head = (cos(t)/5, sin(t)/5)

def init(anim):
    anim.add(
        Vector,
        0, 1/5,
        color='.50',
        update=update_h
    )
    anim.add(
        Vector,
        0, 1/3,
        color='w',
        update=update_m
    )
    anim.add(
        Line,
        0, 0, 0, 1/2,
        color='r',
        lw=1,
        update=update_s
    )

if __name__ == '__main__':
    Animation(
        dt=0.001,
        tmin=0, tmax=1/mHandSpeed,
        init_func=init,
        repeat=False,
        softener=s.smoothstep
    ).play()
