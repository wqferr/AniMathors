import numpy as np

def _clamp(a, b, x):
    return max(a, min(b, x))

def sigmoid(a):
    def base(t):
        return 1 / (1 + np.e**(-a*t)) - .5

    correction = .5 / base(1)
    def f(t):
        t = _clamp(0, 1, t)
        return correction*base(2*t - 1) + .5

    return f

def smoothstep(t):
    t = _clamp(0, 1, t)
    return t*t * (3-2*t)

def poly(a):
    def f(t):
        t = _clamp(0, 1, t)
        return t**a
    return f

def sinexp(a):
    def f(t):
        t = _clamp(0, 1, t)
        return 1 - np.sin(np.pi/2 * np.exp(-a*t*t) * (1-t)*(1-t))
    return f

def bezier3(p):
    """ Creates the Beziér curve (0, p, 1) """
    def f(t):
        return 2*(1-t)*t*p + t*t
    return f

def bezier4(p1, p2):
    """ Creates the Beziér curve (0, p1, p2, 1) """
    def f(t):
        t = _clamp(0, 1, t)
        tc2 = (1-t)*(1-t)
        return 3*tc2*t*p1 + 3*(1-t)*t*t*p2 + t*t*t

    return f

def ease_in(f):
    return bezier3(1/10**f)

def ease_out(f):
    return bezier3(1 - 1/10**f)

def ease_in_out(f):
    f = 1/10**f
    return bezier4(f, 1-f)
