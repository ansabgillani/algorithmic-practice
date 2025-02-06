class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prod_count = {}
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                if product in prod_count:
                    result += prod_count[product]

                if product not in prod_count:
                    prod_count[product] = 0
                prod_count[product] += 1

        return result * 8