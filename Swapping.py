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
            # print("[ ", end = "")
            for job in self.jobs:
                print(self.jobs[job], end=' ')
            # print("]")
            print()
        else:
            print("[ ]")

    def iterate(self, item):
        while item is not None:
            yield item
            item = item.next

    def firstFit(self, pid):
        if pid in self.jobs:
            # get job to do first fit on
            job = self.jobs[pid]
            # get temp variable to hold first segment in linkedlist
            segment = self.segments
            # loop all segments in linkedlist
            while segment is not None:
                # if this segment is a hole that can fit the job
                if int(segment.pid) == 0:
                    #
                    # print("debug 1: " + str(job.size) + " " + str(segment.length))


                    if (int(job.size) <= int(segment.length)):
                        # print("debug 1")



                        #save current hole size for later use
                        size = segment.length
                        # get current segment, change the pid to act as if new segment was added
                        segment.pid = self.pid
                        # get current segment, change the start to act as if new segment was added
                        # in this case, start can stay the same
                        # segment.start =
                        # get current segment, change the len to act as if new segment was added
                        # the len should be the size of the new job
                        segment.length = int(job.size)
                        # set next segment to be the hole but with the new changes to its space
                        # check if there is even room for another hole at end or not
                        if (size - segment.length) == 0:
                            segment.next = None
                        else:
                            segment.next = Segment(0, (segment.start + segment.length), (size - segment.length), None)

                        self.pid += 1
                        # self.segments = temp_segment
                        break
                segment = segment.next

