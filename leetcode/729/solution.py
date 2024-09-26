class MyCalendar:
    def __init__(self):
        # Initialize a list to store booked events as (start, end) tuples
        self.events = []

    def book(self, start: int, end: int) -> bool:
        # Check if the event can be added without causing a double booking
        for s, e in self.events:
            if start < e and s < end:
                return False
        # If no conflict, add the event to the list
        self.events.append((start, end))
        return True

# Example usage:
# myCalendar = MyCalendar()
# print(myCalendar.book(10, 20))  # Output: True
# print(myCalendar.book(15, 25))  # Output: False
# print(myCalendar.book(20, 30))  # Output: True