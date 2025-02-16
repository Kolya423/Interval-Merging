Count task frequencies using Counter().
Use a max-heap to always schedule the most frequent task first.
Track cooldown tasks in a queue with their next available time.
Simulate time unit by unit:
Execute task from the heap.
If not finished, put it in the queue with its cooldown time.
Push tasks back to the heap from the queue when their cooldown ends.
Repeat until all tasks are done, and return the total time.
Key Idea: Prioritize most frequent tasks + manage cooldown with a queue.
