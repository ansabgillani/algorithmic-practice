from typing import List
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # Sort tasks and workers to facilitate binary search
        tasks.sort()
        workers.sort()

        def can_complete(k):
            # Check if we can complete k tasks with the given resources
            remaining_workers = workers[:]
            remaining_pills = pills

            for i in range(k):
                task_strength = tasks[i]
                # Find the smallest worker who can do this task without a pill
                index = bisect.bisect_left(remaining_workers, task_strength)
                if index < len(remaining_workers):
                    # Use this worker
                    remaining_workers.pop(index)
                else:
                    # Try to use a pill on the weakest worker who can still do the task after taking a pill
                    index = bisect.bisect_left(remaining_workers, task_strength - strength)
                    if index < len(remaining_workers) and remaining_pills > 0:
                        remaining_pills -= 1
                        remaining_workers.pop(index)
                    else:
                        # Cannot complete this task with the given resources
                        return False

            return True

        # Binary search to find the maximum number of tasks that can be completed
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_complete(mid):
                left = mid
            else:
                right = mid - 1

        return left