class Solution:
    def sortPeople(self, names, heights):
        combined = list(zip(names, heights))
        sorted_list = sorted(combined, key=lambda x: -x[1])
        return [person[0] for person in sorted_list]