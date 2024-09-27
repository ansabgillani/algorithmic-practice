class Solution:
    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.starts, start)
        bisect.insort(self.ends, end)
        
        i = j = 0
        for _ in range(len(self.starts)):
            if self.starts[i] < self.ends[j]:
                if j - i >= 2:
                    bisect.insort(self.starts, start)
                    bisect.insort(self.ends, end)
                    return False
                j += 1
            else:
                i += 1
        
        return True