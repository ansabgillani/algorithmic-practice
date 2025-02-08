class NumberContainers:
    def __init__(self):
        # Dictionary to store number to set of indices mapping
        self.number_to_indices = {}
        # Dictionary to store index to number mapping
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        # Remove the current index from the old number's set if it exists
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].discard(index)
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        # Update the number to indices mapping and index to number mapping
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = set()
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        # Return the smallest index for the given number or -1 if none exist
        if number in self.number_to_indices and self.number_to_indices[number]:
            return min(self.number_to_indices[number])
        return -1