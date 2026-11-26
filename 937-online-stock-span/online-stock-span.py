class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        p = self.prices
        days = 1
        while p and p[-1][0] <= price:
            _, span = p.pop()
            days += span

        p.append((price, days))
        return days
    
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)