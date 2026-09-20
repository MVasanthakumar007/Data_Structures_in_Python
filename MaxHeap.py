import heapq

jobs = []

n = int(input("Enter number of jobs: "))

for i in range(n):
    job = input("Enter job name: ")
    priority = int(input("Enter job priority: "))
    heapq.heappush(jobs, (priority, job))

print("\nJobs in Heap order:")
for priority, job in jobs:
    print(job, "Priority:", -priority)

print("\nHighest Priority Job:", jobs[0][1])
print("Priority:", -jobs[0][0])

priority, job = heapq.heappop(jobs)

print("\nProcessed Job:", job)
print("Priority:", -priority)

print("\nRemaining jobs:")
for priority, job in jobs:
    print(job, "Priority:", -priority)
