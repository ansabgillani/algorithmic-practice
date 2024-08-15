class Solution:
    def lemonadeChange(self, bills):
        """
        Determines if it is possible to provide correct change for each customer.
        
        :param bills: List of integers representing bills given by customers.
        :return: True if it is possible to provide correct change, False otherwise.
        """
        # Initialize the count of $5 and $10 bills
        five_dollar_bills = 0
        ten_dollar_bills = 0
        
        for bill in bills:
            if bill == 5:
                five_dollar_bills += 1
            elif bill == 10:
                # Check if we have a $5 bill to give as change
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            else:  # bill == 20
                # Try to give the change using one $10 bill and one $5 bill if possible
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    ten_dollar_bills -= 1
                    five_dollar_bills -= 1
                # If not, try giving three $5 bills as change
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
    
        return True