from Segment import Segment
from Job import Job

class Swapping:

    def __init__(self):
        self.size = 100
        self.segments = Segment(0, 0, 100, None)
        self.jobs = {}
        self.pid = 1
        self.next_fit_marker = self.segments

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

    def nextFit(self, pid):
        if pid in self.jobs:
            # get job to do first fit on
            job = self.jobs[pid]
            # get temp variable to hold first segment in linkedlist
            segment = self.next_fit_marker
            # loop all segments in linkedlist
            while segment is not None:
                # if this segment is a hole that can fit the job
                if int(segment.pid) == 0:
                    if (int(job.size) <= int(segment.length)):
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
                        self.next_fit_marker = segment.next
                        self.pid += 1
                        # self.segments = temp_segment
                        break
                segment = segment.next

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
                    if (int(job.size) <= int(segment.length)):
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

                        self.next_fit_marker = segment.next
                        self.pid += 1
                        # self.segments = temp_segment
                        break
                segment = segment.next

    def bestFit(self, pid):
        if pid in self.jobs:
            # keep track of smallest fit
            smallest = None
            segment_ref = None
            # get job to do first fit on
            job = self.jobs[pid]
            # get temp variable to hold first segment in linkedlist
            segment = self.segments
            # loop all segments in linkedlist
            while segment is not None:
                # make sure segment is a hole
                if int(segment.pid) == 0:
                    # make sure the difference between the spaces is the smallest or not zero
                    # e.g. if you have 25 space in one segment, and 27 in another, and job takes up 24
                    # 25 - 24 == 1 and 27 - 24 == 3, so the one with smallest difference is the best fit
                    if smallest == None or int(smallest) > (int(segment.length) - int(job.size)):
                        # must also make sure it is not zero
                        if int(segment.length) - int(job.size) >= 0:
                            # set variables to keep record
                            smallest = (int(segment.length) - int(job.size))
                            segment_ref = segment
                # get next reference
                segment = segment.next
            #save current hole size for later use
            size = segment_ref.length
            # get current segment, change the pid to act as if new segment was added
            segment_ref.pid = self.pid
            # get current segment, change the start to act as if new segment was added
            # in this case, start can stay the same
            # segment.start =
            # get current segment, change the len to act as if new segment was added
            # the len should be the size of the new job
            segment_ref.length = int(job.size)
            # set next segment to be the hole but with the new changes to its space
            # check if there is even room for another hole at end or not
            if (size - segment_ref.length) == 0:
                segment_ref.next = None
            else:
                segment_ref.next = Segment(0, (segment_ref.start + segment_ref.length), (size - segment_ref.length), None)
            self.pid += 1


    def worstFit(self, pid):
        if pid in self.jobs:
            # keep track of smallest fit
            biggest = None
            segment_ref = None
            # get job to do first fit on
            job = self.jobs[pid]
            # get temp variable to hold first segment in linkedlist
            segment = self.segments
            # loop all segments in linkedlist
            while segment is not None:
                # make sure segment is a hole
                if int(segment.pid) == 0:
                    # make sure the difference between the spaces is the smallest or not zero
                    # e.g. if you have 25 space in one segment, and 27 in another, and job takes up 24
                    # 25 - 24 == 1 and 27 - 24 == 3, so the one with smallest difference is the best fit
                    if biggest == None or int(biggest) < (int(segment.length) - int(job.size)):
                        # must also make sure it is not zero
                        if int(segment.length) - int(job.size) >= 0:
                            # set variables to keep record
                            biggest = (int(segment.length) - int(job.size))
                            segment_ref = segment
                # get next reference
                segment = segment.next
            #save current hole size for later use
            size = segment_ref.length
            # get current segment, change the pid to act as if new segment was added
            segment_ref.pid = self.pid
            # get current segment, change the start to act as if new segment was added
            # in this case, start can stay the same
            # segment.start =
            # get current segment, change the len to act as if new segment was added
            # the len should be the size of the new job
            segment_ref.length = int(job.size)
            # set next segment to be the hole but with the new changes to its space
            # check if there is even room for another hole at end or not
            if (size - segment_ref.length) == 0:
                segment_ref.next = None
            else:
                segment_ref.next = Segment(0, (segment_ref.start + segment_ref.length), (size - segment_ref.length), None)
            self.pid += 1



