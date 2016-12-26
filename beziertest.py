
from core.anim import Animation
from core.obj import Curve
from core.soft import bezier, smoothstep

bx = bezier([1, 1, 0, .5, 0, 0, 0, 0, 0, 0])
by = bezier([.2, 0, 0, 0])

def update_c(c, t, dt):
    c.tmax = t

def init(anim):
    anim.add(
        Curve,
        lambda t: (bx(t), by(t)),
        0, 0,
        color='w',
        update=update_c
    )

if __name__ == '__main__':
    anim = Animation(
        xlim=(0, 1), ylim=(0, 1),
        init_func=init,
        softener=smoothstep,
        repeat=False
    )
    anim.play()
