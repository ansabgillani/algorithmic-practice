class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        totalDrinks = numBottles
        while totalDrinks >= numExchange:
            newFullBottles = totalDrinks // numExchange
            totalDrinks += newFullBottles
            totalDrinks -= newFullBottles * numExchange
        return totalDrinks

# Example usage:
sol = Solution()
print(sol.numWaterBottles(9, 3))  # Output: 13
print(sol.numWaterBottles(15, 4))  # Output: 19