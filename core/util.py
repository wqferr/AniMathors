def to_r2(f):
    return lambda t: (t, f(t))
