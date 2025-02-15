class MyCalendar:
    def __init__(self):
        # Initialize a list to store events sorted by start time
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Find the correct position to insert the new event using binary search
        left, right = 0, len(self.events)
        
        while left < right:
            mid = (left + right) // 2
            if self.events[mid][1] <= start:
                left = mid + 1
            else:
                right = mid
        
        # Check if the new event can be inserted without causing a conflict
        if left == len(self.events):
            self.events.append((start, end))
            return True
        
        if start < self.events[left][0]:
            self.events.insert(left, (start, end))
            return True
        
        return False

# Example usage:
if __name__ == "__main__":
    my_calendar = MyCalendar()
    print(my_calendar.book(10, 20))  # Output: True
    print(my_calendar.book(15, 25))  # Output: False
    print(my_calendar.book(20, 30))  # Output: True