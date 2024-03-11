class Solution:
    def customSortString(self, order, s):
        order_map = {char: idx for idx, char in enumerate(order)}
        sorted_s = sorted(s, key=lambda x: (order_map.get(x, float('inf')), x))
        return ''.join(sorted_s)