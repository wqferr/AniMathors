from matplotlib.colors import colorConverter as cc

origin = (0, 0)

class Point(object):
    def __init__(self, ax, x=None, y=None, **kwargs):
        self._update_func = kwargs.get('update', lambda p,t: None)

        if None in [x, y]:
            x, y = 0, 0

        dot, = ax.plot([float(x)], [float(y)], 'o')
        dot.set_markeredgewidth(0)
        self._dot = dot

        self.color = kwargs.get('color', '0')
        self.size = kwargs.get('size', 10)

    def __del__(self):
        del self._dot

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._dot.__getattribute__(attr)

    def update(self, t):
        self._update_func(self, t)

    @property
    def pos(self):
        return self._dot.get_data()

    @pos.setter
    def pos(self, p):
        self._dot.set_data(p[0], p[1])

    @property
    def x(self):
        return self._dot.get_xdata()

    @property
    def y(self):
        return self._dot.get_ydata()

    @x.setter
    def x(self, v):
        self._dot.set_xdata(v)

    @y.setter
    def y(self, v):
        self._dot.set_ydata(v)

    @property
    def color(self):
        return self._dot.get_markerfacecolor()

    @color.setter
    def color(self, c):
        c = cc.to_rgb(c)
        self._dot.set_markerfacecolor(c)
        self._dot.set_markerfacecoloralt(c)

    @property
    def size(self):
        return self._dot.get_markersize()

    @size.setter
    def size(self, r):
        self._dot.set_markersize(r)


class Line(object):
    def __init__(self, ax, x1=None, y1=None, x2=None, y2=None, **kwargs):
        self._update_func = kwargs.get('update', lambda l,t: None)
        if None in [x1, y1, x2, y2]:
            x1, y1, x2, y2 = 0, 0, 0, 0

        self._seg, = ax.plot([float(x1), float(x2)], [float(y1), float(y2)], '-')
        self.color = kwargs.get('color', '0')

    def __del__(self):
        del self._seg

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._seg.__getattribute__(attr)

    def update(self, t):
        self._update_func(self, t)

    @property
    def color(self):
        return self._seg.get_color()

    @color.setter
    def color(self, c):
        c = cc.to_rgb(c)
        self._seg.set_color(c)

    @property
    def pos1(self):
        return self.x1, self.y1

    @pos1.setter
    def pos1(self, p):
        self.x1, self.y1 = p

    @property
    def pos2(self):
        return self.x2, self.y2

    @pos2.setter
    def pos2(self, p):
        self.x2, self.y2 = p

    @property
    def x1(self):
        return self._seg.get_xdata()[0]

    @x1.setter
    def x1(self, x):
        self._seg.set_xdata([x, self.x2])

    @property
    def x2(self):
        return self._seg.get_xdata()[1]

    @x2.setter
    def x2(self, x):
        self._seg.set_xdata([self.x1, x])

    @property
    def y1(self):
        return self._seg.get_ydata()[0]

    @y1.setter
    def y1(self, y):
        self._seg.set_ydata([y, self.y2])

    @property
    def y2(self):
        return self._seg.get_ydata()[1]

    @y2.setter
    def y2(self, y):
        self._seg.set_ydata([self.y1, y])
