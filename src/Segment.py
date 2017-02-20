class Segment:

    def __init__(self, pid, start, length, next):
        self.pid = pid
        self.start = start
        self.length = length
        # next will be of type Segment
        self.next = next

    @property
    def pid(self):
        return self.pid

    @pid.setter
    def pid(self, value):
        self.pid = value

    @property
    def start(self):
        return self.start

    @start.setter
    def start(self, value):
        self.start = value

    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, value):
        self.length = value

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, value):
        self.next = value

    # https://pyformat.info/
    def __repr__(self):
        return '{} {} {}'.format(self.pid, self.start, self.length)
