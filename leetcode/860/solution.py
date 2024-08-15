class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Determines if it is possible to give correct change for each bill in the order they are given.

        :param bills: List of integers representing bills given by customers.
        :return: True if all customers receive correct change, False otherwise.
        """
        five_dollar = 0
        ten_dollar = 0
        
        for bill in bills:
            if bill == 5:
                five_dollar += 1
            elif bill == 10:
                if five_dollar == 0:
                    return False
                five_dollar -= 1
                ten_dollar += 1
            else:  # bill == 20
                if ten_dollar > 0 and five_dollar > 0:
                    ten_dollar -= 1
                    five_dollar -= 1
                elif five_dollar >= 3:
                    five_dollar -= 3
                else:
                    return False
        
        return True