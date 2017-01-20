from math import ceil
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Animation(object):

    def __init__(self, *args, **kwargs):
        self._fig, self._ax = plt.subplots()
        self._fig.set_facecolor(kwargs.get('facecolor', 'black'))

        self._ax.set_xlim(*kwargs.get('xlim', (-1, 1)))
        self._ax.set_ylim(*kwargs.get('ylim', (-1, 1)))
        self._fig.set_size_inches(8, 8, forward=True)
        plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
        self._ax.axis('off')

        self._dt = float(kwargs.get('dt', 0.01))
        self._speed = float(kwargs.get('speed', 1))
        self._len = kwargs.get('length', 1)
        self._repeat = kwargs.get('repeat', False)
        self._softener = kwargs.get('softener', lambda t: t)

        self._init_func = kwargs.get('init_func', lambda: None)

        self._objects = []
        self._anim = None

    def __del__(self):
        self._reset()
        del self._fig
        del self._ax

    def create(self, objType, *args, **kwargs):
        obj = objType(self._ax, *args, **kwargs)
        self._objects.append(obj)
        return obj

    def add(self, obj):
        self._objects.append(obj)
        return obj

    def _reset(self):
        for obj in self._objects:
            obj.remove()
        self._objects = []

    def _init(self):
        self._reset()
        self._init_func(self)
        return self._objects

    def _run(self, t):
        t = self._dt * t * self._speed
        t = self._softener(t / self._len) * self._len
        for obj in self._objects:
            obj.anim_update(t, self._len)
        return self._objects

    def play(self, **kwargs):
        kwargs['init_func'] = self._init
        kwargs.setdefault('interval', self._dt/self._speed)
        kwargs['frames'] = ceil((self._len/self._dt) / self._speed)
        kwargs.setdefault('repeat', self._repeat)
        self._anim = anim.FuncAnimation(self._fig, self._run, **kwargs)
        plt.show()

    @property
    def dt(self):
        return self._dt

