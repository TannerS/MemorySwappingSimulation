class Job:

    def __init__(self, pid, size):
        self.pid = pid
        self.size = size

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    # https://pyformat.info/
    def __repr__(self):
        return '[{} {}]'.format(self.pid, self.size)
