class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for booking in self.bookings:
            if not (end <= booking[0] or start >= booking[1]):
                return False
        self.bookings.append([start, end])
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)