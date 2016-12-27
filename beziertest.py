from core.anim import Animation
from core.obj import Curve
from core.soft import bezier, smoothstep, bezier_s

def update_c(c, t, tmax):
    c.tmax = t

def init(anim):
    B = []

    for i in range(5):
        B.append(bezier_s(i+1))

    for b in B:
        anim.add(
            Curve,
            lambda t, b=b: (t, b(t)),
            0, 0,
            update=update_c
        )
        anim.add(
            Curve,
            lambda t, b=b: (b(t), t),
            0, 0,
            update=update_c
        )
        anim.add(
            Curve,
            lambda t, b=b: (t, b(1-t)),
            0, 0,
            update=update_c
        )
        anim.add(
            Curve,
            lambda t, b=b: (b(t), 1-t),
            0, 0,
            update=update_c
        )

if __name__ == '__main__':
    anim = Animation(
        dt=.005, length=1,
        speed=2,
        xlim=(0, 1), ylim=(0, 1),
        init_func=init,
        softener=smoothstep
    )
    anim.play()
