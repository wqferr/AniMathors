import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as anim

origin = numpy.array([0, 0])

class Point(object):
    def __init__(self, ax, x, y, **kwargs):
        self._path_func = kwargs.get('path', lambda t,dt: origin)
        self._prevMov = origin

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

    def update(self, t, dt):
        mov = self._path_func(t, dt)
        dx = (self._prevMov[0]+mov[0]) / 2
        dy = (self._prevMov[1]+mov[1]) / 2
        self.x += dt*dx
        self.y += dt*dy
        self._prevMov = mov

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
        self._dot.set_markerfacecolor(c)
        self._dot.set_markerfacecoloralt(c)

    @property
    def size(self):
        return self._dot.get_markersize()

    @size.setter
    def size(self, r):
        self._dot.set_markersize(r)


class Animation(object):

    def __init__(self, *args, **kwargs):
        self._fig, self._ax = plt.subplots()
        self._fig.set_facecolor(kwargs.get('facecolor', 'black'))

        self._ax.set_xlim(*kwargs.get('xlim', (-1, 1)))
        self._ax.set_ylim(*kwargs.get('ylim', (-1, 1)))
        self._ax.axis('off')

        self._dt = kwargs.get('dt', 0.01)

        self._init_func = kwargs.get('init_func', lambda: None)

        self._anim = None
        self._objects = []

    def __del__(self):
        self._reset()
        del self._fig
        del self._ax

    def add(self, objType, *args, **kwargs):
        self._objects.append(objType(self._ax, *args, **kwargs))

    def _reset(self):
        for obj in self._objects:
            obj.remove()
        self._objects = []

    def _init(self):
        self._reset()
        self._init_func(self)
        return self._objects

    def _run(self, t):
        t *= self._dt
        for obj in self._objects:
            obj.update(t, self._dt)
        return self._objects

    def play(self, **kwargs):
        kwargs['init_func'] = self._init
        self._anim = anim.FuncAnimation(self._fig, self._run, **kwargs)
        plt.show()
