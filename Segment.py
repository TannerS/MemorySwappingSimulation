# http://stackoverflow.com/questions/18989362/python-property-setting-from-list-causes-maximum-recursion-depth-exceeded

class Segment:

    def __init__(self, pid, start, length, next):
        self.pid = pid
        self.start = start
        self.length = length
        self.next = next

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    # https://pyformat.info/
    def __repr__(self):
        return '{} {} {}'.format(self.pid, self.start, self.length)





