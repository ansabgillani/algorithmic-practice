class Solution:
    def finalPrices(self, prices):
        for i, price in enumerate(prices):
            discount = next((prices[j] for j in range(i + 1, len(prices)) if prices[j] <= price), 0)
            prices[i] -= discount

        return prices