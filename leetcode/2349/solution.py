class Solution:
    def __init__(self):
        # Dictionary to map numbers to their smallest indices
        self.index_map = {}
        # Dictionary to store sets of indices for each number, allowing quick access to the smallest index
        self.number_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            self.number_indices[old_number].remove(index)
            if not self.number_indices[old_number]:
                del self.number_indices[old_number]
        
        self.index_map[index] = number
        if number not in self.number_indices:
            self.number_indices[number] = set()
        self.number_indices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_indices and self.number_indices[number]:
            return min(self.number_indices[number])
        else:
            return -1