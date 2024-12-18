class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        
        # Iterate over each price from right to left
        for i in range(n-1, -1, -1):
            # Maintain a decreasing stack of prices
            while stack and prices[i] < stack[-1]:
                stack.pop()
            # If stack is not empty, apply the discount
            if stack:
                prices[i] -= stack[-1]
            # Push the current price onto the stack
            stack.append(prices[i])
        
        return prices