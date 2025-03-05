class MyCalendar:
    def __init__(self):
        # Initialize a list to store events, sorted by start time
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Find the position where the new event should be inserted
        i = bisect.bisect_left(self.events, (start, end))
        
        # Check if the new event overlaps with any existing events
        if i > 0 and self.events[i-1][1] > start:
            return False
        if i < len(self.events) and self.events[i][0] < end:
            return False
        
        # Insert the new event into the list
        self.events.insert(i, (start, end))
        return True

# Test cases to verify the solution
myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # Output: True
print(myCalendar.book(15, 25))  # Output: False
print(myCalendar.book(20, 30))  # Output: True