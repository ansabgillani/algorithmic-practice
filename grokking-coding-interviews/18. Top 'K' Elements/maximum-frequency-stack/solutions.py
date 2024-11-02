class FreqStack:
    def __init__(self):
        self.freq = {}  # Frequency of each element
        self.group = defaultdict(list)  # Group elements by their frequency
        self.max_freq = 0  # Maximum frequency seen so far

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        self.freq[val] -= 1
        return val

# Example usage
# freqStack = FreqStack()
# freqStack.push(5)
# freqStack.push(7)
# freqStack.push(5)
# freqStack.push(7)
# freqStack.push(4)
# print(freqStack.pop())  # Output: 7
# print(freqStack.pop())  # Output: 7
# print(freqStack.pop())  # Output: 5
# print(freqStack.pop())  # Output: 5