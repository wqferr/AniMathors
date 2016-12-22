import numpy as np
from src.core import Animation

def init(anim):
    anim.add_point(
        0., np.sin(0),
        color='b', size=10,
        path=lambda t,dt: (0, np.cos(t))
    )
    anim.add_point(
        np.cos(0), 0.,
        color='g', size=10,
        path=lambda t,dt: (-np.sin(t), 0)
    )
    anim.add_point(
        1., 0.,
        color='y', size=5,
        path=lambda t,dt: (-np.sin(t), 2*np.cos(2*t))
    )

if __name__ == '__main__':
    anim = Animation(dt=0.01*np.pi, init_func=init)
    anim.play(interval=100/6, frames=200)
