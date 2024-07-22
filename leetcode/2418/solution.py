class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Combine names and heights into pairs and sort by height in descending order
        combined = sorted(zip(names, heights), key=lambda x: -x[1])
        # Extract the sorted names from the pairs
        return [person[0] for person in combined]