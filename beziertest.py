from core.anim import Animation
from core.obj import Curve
from core.soft import bezier_s, bezier_z, smoothstep, sigmoid
from core.util import to_r2

def update_c(c, t, dt):
    c.tmax = t

def init(anim):
    anim.add(
        Curve,
        to_r2(bezier_s(3)),
        0, 0,
        update=update_c
    )
    anim.add(
        Curve,
        to_r2(bezier_z(3)),
        0, 0,
        update=update_c
    )

if __name__ == '__main__':
    anim = Animation(
        dt=.01, length=1,
        speed=1/2,
        xlim=(-2, 2), ylim=(-2, 2),
        init_func=init,
        softener=smoothstep
    )
    anim.play()
