class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1
        
        max_freq = max(freq.values())
        n_max_freq = list(freq.values()).count(max_freq)
        
        return max((max_freq - 1) * (n + 1) + n_max_freq, len(tasks))