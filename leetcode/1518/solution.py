class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Calculate the maximum number of water bottles that can be drunk.
        
        :param numBottles: Initial number of full water bottles
        :param numExchange: Number of empty bottles needed to exchange for one full bottle
        :return: Maximum number of water bottles that can be drunk
        """
        total_drunk = 0
        empty_bottles = 0
        
        while numBottles > 0:
            # Drink all the bottles and collect the empty ones
            total_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0
            
            # Exchange empty bottles for full ones
            while empty_bottles >= numExchange:
                numBottles += empty_bottles // numExchange
                empty_bottles %= numExchange
        
        return total_drunk