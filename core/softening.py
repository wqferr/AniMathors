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
