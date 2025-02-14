class Solution:
    # Initialize an empty list to store cumulative products and a variable to track zero positions
    def __init__(self):
        self.products = [1]
        self.zero_pos = -1

    # Add a number to the stream and update the cumulative product list accordingly
    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
            self.zero_pos = len(self.products) - 1
        else:
            self.products.append(self.products[-1] * num)

    # Get the product of the last k numbers in the stream
    def getProduct(self, k: int) -> int:
        n = len(self.products)
        if k > n or self.zero_pos >= (n-k):
            return 0
        else:
            return self.products[-1] // self.products[n-k-1]