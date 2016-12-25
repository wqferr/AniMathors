import numpy as np

def _clamp(a, b, x):
    return max(a, min(b, x))

def sigmoid(k):
    def base(t):
        return 1 / (1 + np.e**(-k*t)) - .5

    correction = .5 / base(1)
    def f(t):
        t = _clamp(0, 1, t)
        return correction * base(2*t - 1) + .5

    return f
