import numpy as np
from core.anim import Animation
from core.obj import Point, Line

def init(anim):
    anim.add(
        Point,
        0, np.sin(0),
        color='b', size=10,
        path=lambda t,dt: (0, np.sin(3*t))
    )
    anim.add(
        Point,
        np.cos(0), 0,
        color='g', size=10,
        path=lambda t,dt: (np.cos(t), 0)
    )
    anim.add(
        Point,
        1, 0,
        color='w', size=5,
        path=lambda t,dt: (np.cos(t), np.sin(3*t))
    )
    anim.add(
        Line,
        -.5, 0,
        .5, 0,
        color='r',
        path = lambda t,dt: (
            (np.cos(t), np.sin(t)),
            (-np.cos(t), -np.sin(t))
        )
    )

if __name__ == '__main__':
    anim = Animation(dt=0.01*np.pi, init_func=init)
    anim.play(interval=100/6, frames=200)
