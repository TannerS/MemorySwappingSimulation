class Segment:

    def __init__(self, pid, size):
        self.pid = pid
        self.size = size

    @property
    def pid(self):
        return self.pid

    @pid.setter
    def pid(self, value):
        self.pid = value

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.size = value

    # https://pyformat.info/
    def __repr__(self):
        return '[{} {}]'.format(self.pid, self.size)
