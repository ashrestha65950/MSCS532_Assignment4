import heapq
import time

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # This ensures the heap pops the highest priority task
        return self.priority > other.priority

    def __repr__(self):
        return f"Task({self.task_id}, P={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_max(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def increase_priority(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                break
        heapq.heapify(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
if __name__ == "__main__":
    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task("T1", priority=5, arrival_time=0, deadline=10))
    pq.insert(Task("T2", priority=8, arrival_time=1, deadline=5))
    pq.insert(Task("T3", priority=3, arrival_time=2, deadline=8))

    print("Initial task queue:")
    print(pq.heap)

    # Extract tasks by priority
    print("\nScheduling tasks:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Running {task}")

    # Priority change simulation
    pq.insert(Task("T4", priority=4, arrival_time=3, deadline=6))
    pq.insert(Task("T5", priority=2, arrival_time=4, deadline=7))
    pq.increase_priority("T5", new_priority=9)
    print("\nAfter priority update:")
    while not pq.is_empty():
        print(pq.extract_max())
