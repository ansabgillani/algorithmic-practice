import heapq

def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    # Count the frequency of each task
    task_count = list(heapq._heapify_max([-v for v in collections.Counter(tasks).values()]))
    
    max_task_freq = -task_count[0]
    idle_slots = (max_task_freq - 1) * n
    
    for freq in task_count:
        if freq == -max_task_freq:
            idle_slots -= (max_task_freq - 1)
            
    return max(len(tasks), max_task_freq + idle_slots)

# Example usage:
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))  # Output: 8