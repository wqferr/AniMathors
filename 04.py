from core.obj import Polygon
from core.anim import Animation
from numpy import pi, sin, cos

def init(anim):
    global p
    p = anim.create(
        Polygon, 
        [
            (cos(0), sin(0)),
            (cos(2*pi/3), sin(2*pi/3)),
            (cos(4*pi/3), sin(4*pi/3))
        ]
    )

if __name__ == '__main__':
    global anim
    anim = Animation(
        length=2.,
        init_func=init,
        repeat=True
    )
    anim.play()
