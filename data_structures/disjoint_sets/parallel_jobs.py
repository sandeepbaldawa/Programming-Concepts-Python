'''
Problem Introduction
In this problem you will simulate a program that processes a list of jobs in parallel.
Problem Description
Task. You have a program which is parallelized and uses n independent threads to process the given list
of m jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t
interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
will it take any thread to process this job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it start processing.

Sample 1.
Input:
2 5
1 2 3 4 5
Output:
0 0
1 0
0 1
1 2
0 4
Explanation:
1. The two threads try to simultaneously take jobs from the list, so thread with index 0 actually
takes the first job and starts working on it at the moment 0.
2. The thread with index 1 takes the second job and starts working on it also at the moment 0.
3. After 1 second, thread 0 is done with the first job and takes the third job from the list, and starts
processing it immediately at time 1.
4. One second later, thread 1 is done with the second job and takes the fourth job from the list, and
starts processing it immediately at time 2.
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-
import heapq


class JobQueue:

    def read_data(self):
        (self.num_workers, m) = (4, 20)  # map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.heap = []
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print (self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):

        # TODO: replace this code with a faster algorithm.

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(self.num_workers):
            heapq.heappush(self.heap, (next_free_time[i], i))
        for i in range(len(self.jobs)):
            next_worker = 0
            (w, next_worker) = heapq.heappop(self.heap)
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]
            heapq.heappush(self.heap, (next_free_time[next_worker],
                           next_worker))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


__name__ = '__main__'
if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
