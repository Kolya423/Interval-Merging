from collections import Counter
import heapq

def least_interval(tasks, n):
    task_counts = Counter(tasks)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = []  # pairs of (time_available, -count)

    while max_heap or queue:
        time += 1

        if max_heap:
            current_task_count = heapq.heappop(max_heap) + 1  # Execute the task
            if current_task_count != 0:
                queue.append((time + n, current_task_count))

        if queue and queue[0][0] == time:
            heapq.heappush(max_heap, queue.pop(0)[1])

    return time

# Example usage
tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2
print(least_interval(tasks, n))  # Output: 8
