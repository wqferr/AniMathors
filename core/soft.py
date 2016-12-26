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

def bezier(points):
    points = list(points) # preserve original list
    n = len(points)
    def f(t):
        p = list(points)
        for k in range(1, n):
            for i in range(n-k):
                p[i] = (1-t)*p[i] + t*p[i+1]
        return p[0]

    return f

def bezier_s(order):
    return bezier([0]*order + [1]*order)

def bezier_z(order):
    return bezier([1]*order + [0]*order)

def ease_in(f):
    return bezier3(1/10**f)

def ease_out(f):
    return bezier3(1 - 1/10**f)

def ease_in_out(f):
    f = 1/10**f
    return bezier4(f, 1-f)
