class MyCalendarTwo:
    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if adding this booking causes a triple booking
        for s, e in self.double_bookings:
            if max(start, s) < min(end, e):
                return False
        
        # Add to single bookings first
        i = 0
        while i < len(self.single_bookings):
            s, e = self.single_bookings[i]
            if end <= s: break
            if start >= e:
                i += 1
                continue
            
            # Merge overlapping intervals
            if max(start, s) < min(end, e):
                self.double_bookings.append([max(start, s), min(end, e)])
                end = max(end, e)
            
            i += 1
        
        self.single_bookings.append([start, end])
        return True

# Example usage:
myCalendarTwo = MyCalendarTwo()
print(myCalendarTwo.book(10, 20))  # True
print(myCalendarTwo.book(50, 60))  # True
print(myCalendarTwo.book(10, 40))  # True
print(myCalendarTwo.book(5, 15))   # False
print(myCalendarTwo.book(5, 10))   # True
print(myCalendarTwo.book(25, 55))  # True