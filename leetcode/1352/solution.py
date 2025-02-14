class ProductOfNumbers:
    def __init__(self):
        # Initialize a list to store cumulative products
        self.products = [1]

    def add(self, num: int) -> None:
        # If the number is zero, reset the product list
        if num == 0:
            self.products = [1]
        else:
            # Append the cumulative product of the current number and the last product
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If there are fewer than k elements, return 0
        if len(self.products) <= k:
            return 0
        else:
            # Return the product of the last k numbers using cumulative products
            return self.products[-1] // self.products[-k-1]