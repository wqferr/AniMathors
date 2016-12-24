import numpy as np
from matplotlib.colors import colorConverter as cc
from numpy import sqrt, arctan2, pi, sin, cos

class Point(object):
    def __init__(self, ax, x, y, **kwargs):
        self._update_func = kwargs.get('update', lambda p,t,dt: None)

        dot, = ax.plot([float(x)], [float(y)], 'o')
        dot.set_markeredgewidth(0)
        self._dot = dot

        self.color = kwargs.get('color', 'w')
        self.size = kwargs.get('size', 10)

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._dot.__getattribute__(attr)

    def update(self, t, dt):
        self._update_func(self, t, dt)

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
    def __init__(self, ax, x1, y1, x2, y2, **kwargs):
        self._update_func = kwargs.get('update', lambda l,t,dt: None)

        self._seg, = ax.plot([float(x1), float(x2)], [float(y1), float(y2)], '-')
        self.color = kwargs.get('color', 'w')
        self.lw = kwargs.get('lw', 2)

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._seg.__getattribute__(attr)

    def update(self, t, dt):
        self._update_func(self, t, dt)

    @property
    def color(self):
        return self._seg.get_color()

    @color.setter
    def color(self, c):
        c = cc.to_rgb(c)
        self._seg.set_color(c)

    @property
    def lw(self):
        return self._seg.get_linewidth()

    @lw.setter
    def lw(self, w):
        self._seg.set_linewidth(w)

    @property
    def p1(self):
        return self.x1, self.y1

    @p1.setter
    def p1(self, p):
        self.x1, self.y1 = p

    @property
    def p2(self):
        return self.x2, self.y2

    @p2.setter
    def p2(self, p):
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

class Vector(object):
    def __init__(self, ax, x, y, dx=None, dy=None, **kwargs):
        self._update_func = kwargs.get('update', lambda v,t,dt: None)
        if None in [dx, dy]:
            dx, dy = x, y
            x, y = 0, 0

        self.norm2 = dx**2 + dy**2
        self.norm = sqrt(self.norm2)

        self.head_angle = kwargs.get('head_angle', pi/6)
        self.head_length = kwargs.get('head_length', self.norm/5)

        self._arrow = []
        hx, hy = x+dx, y+dy
        angle = arctan2(dy, dx)
        self._arrow.append(Line(ax, x, y, hx, hy, **kwargs))
        self._arrow.append(Line(
            ax,
            hx, hy,
            0, 0,
            **kwargs
        ))
        self._arrow.append(Line(
            ax,
            hx, hy,
            0, 0,
            **kwargs
        ))
        self._update_arrow_head()

        self.color = kwargs.get('color', 'w')

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._arrow[0].__getattribute__(attr)

    def remove(self):
        for obj in self._arrow:
            obj.remove()

    def _update_arrow_head(self):
        self._arrow[1].p1 = self._arrow[0].p2
        self._arrow[1].p2 = self._head_shaft_pos(-1)
        self._arrow[2].p1 = self._arrow[0].p2
        self._arrow[2].p2 = self._head_shaft_pos(1)

    def _head_shaft_pos(self, direction):
        angle = arctan2(self.hy-self.y, self.hx-self.x)
        a = self.head_angle
        b = angle - pi

        t = a*direction + b
        return self.hx+cos(t)*self.head_length, self.hy+sin(t)*self.head_length

    def update(self, t, dt):
        self._update_func(self, t, dt)

    @property
    def color(self):
        return self._arrow[0].get_color()

    @color.setter
    def color(self, c):
        c = cc.to_rgb(c)
        for obj in self._arrow:
            obj.set_color(c)

    @property
    def lw(self):
        return self._arrow[0].lw

    @lw.setter
    def lw(self, w):
        for obj in self._arrow:
            obj.lw = w

    @property
    def x(self):
        return self._arrow[0].x1

    @x.setter
    def x(self, v):
        dx = v - self.x
        for obj in self._arrow:
            obj.x1 += dx
            obj.x2 += dx

    @property
    def y(self):
        return self._arrow[0].y1

    @y.setter
    def y(self, v):
        dy = v - self.y
        for obj in self._arrow:
            obj.y1 += dy
            obj.y2 += dy

    @property
    def dx(self):
        return self.hx - self.x

    @dx.setter
    def dx(self, d):
        self.hx = self.x+d

    @property
    def dy(self):
        return self.hy - self.y

    @dy.setter
    def dy(self, d):
        self.hy = self.y+d

    @property
    def hx(self):
        return self._arrow[0].x2

    @hx.setter
    def hx(self, v):
        self._arrow[0].x2 = v
        self._update_arrow_head()

    @property
    def hy(self):
        return self._arrow[0].y2

    @hy.setter
    def hy(self, v):
        self._arrow[0].y2 = v
        self._update_arrow_head()

    @property
    def head(self):
        return self.hx, self.hy

    @head.setter
    def head(self, p):
        self.hx, self.hy = p

    @property
    def tail(self):
        return self.x, self.y

    @tail.setter
    def tail(self, p):
        self.x, self.y = p

class Curve(object):
    def __init__(self, ax, f, tmin=0, tmax=1, dt=0.01, **kwargs):
        self._update_func = kwargs.get('update', lambda c,t,dt: None)
        self._f = f
        self._tmin = tmin
        self._tmax = tmax
        self._dt = dt
        self._line, = ax.plot([], [])
        self._update_line()
        self.color = kwargs.get('color', 'w')

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            return self._line.__getattribute__(attr)

    @property
    def color(self):
        return self._line.get_color()

    @color.setter
    def color(self, c):
        c = cc.to_rgb(c)
        self._line.set_color(c)

    def update(self, t, dt):
        self._update_func(self, t, dt)

    def update_params(self, **kwargs):
        if 'tmin' in kwargs:
            self._tmin = kwargs['tmin']
        if 'tmax' in kwargs:
            self._tmax = kwargs['tmax']
        if 'dt' in kwargs:
            self._dt = kwargs['dt']

        self._update_line()

    def _update_line(self):
        T, F = [], []
        t = self.tmin
        while t < self.tmax:
            T.append(t)
            F.append(self.f(t))
            t += self.dt

        self._line.set_xdata(T)
        self._line.set_ydata(F)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, func):
        self._f = func
        self._update_line()

    @property
    def tmin(self):
        return self._tmin

    @tmin.setter
    def tmin(self, t):
        self._tmin = t
        self._update_line()

    @property
    def tmax(self):
        return self._tmax

    @tmax.setter
    def tmax(self, t):
        self._tmax = t
        self._update_line()

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, d):
        self._dt = d
        self._update_func()

    @property
    def p1(self):
        return self._line.get_xdata()[0], self._line.get_ydata()[0]

    @property
    def p2(self):
        return self._line.get_xdata()[-1], self._line.get_ydata()[-1]
