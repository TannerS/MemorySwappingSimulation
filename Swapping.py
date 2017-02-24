from Segment import Segment
from Job import Job

class Swapping:

    def __init__(self):
        self.size = 100
        self.segments = Segment(0, 0, 100, None)
        self.jobs = {}
        self.pid = 1

    def add(self, pid, size):
        self.jobs[pid] = Job(pid, size)

    def listSegments(self):
        for segment in self.iterate(self.segments):
            print(segment, end=' ')
        print()

    def listJobs(self):
        if(len(self.jobs) > 0):
            print("[ ", end = "")
            for job in self.jobs:
                print(job, end=' ')
            print("]")
            print()
        else:
            print("[ ]")

    def iterate(self, item):
        while item is not None:
            yield item
            item = item.next