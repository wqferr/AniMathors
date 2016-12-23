import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Animation(object):

    def __init__(self, *args, **kwargs):
        self._fig, self._ax = plt.subplots()
        self._fig.set_facecolor(kwargs.get('facecolor', 'black'))

        self._ax.set_xlim(*kwargs.get('xlim', (-1, 1)))
        self._ax.set_ylim(*kwargs.get('ylim', (-1, 1)))
        self._fig.set_size_inches(10, 10, forward=True)
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
        return self._objects[-1]

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
            obj.update(t)
        return self._objects

    def play(self, **kwargs):
        kwargs['init_func'] = self._init
        self._anim = anim.FuncAnimation(self._fig, self._run, **kwargs)
        plt.show()
