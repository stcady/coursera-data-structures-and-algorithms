# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(num_workers, jobs):
    assigned_jobs = [None] * len(jobs)
    next_start_time = [0] * num_workers
    heap = []
    for i in range(num_workers):
        heapq.heappush(heap, (next_start_time[i], i))
    for i in range(len(jobs)):
        _, curr_worker = heapq.heappop(heap)
        assigned_jobs[i] = AssignedJob(curr_worker, next_start_time[curr_worker])
        next_start_time[curr_worker] += jobs[i]
        heapq.heappush(heap, (next_start_time[curr_worker], curr_worker))
    return assigned_jobs


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
