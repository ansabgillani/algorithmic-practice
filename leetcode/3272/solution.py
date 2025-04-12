from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Generate a list of all digits from 0 to 9
        digits = [str(i) for i in range(10)]
        
        # Function to calculate permutations of multiset
        def perm(multiset):
            total = factorial(sum(multiset.values()))
            for count in multiset.values():
                total //= factorial(count)
            return total
        
        good_count = 0
        
        # Try all combinations of digits with sum divisible by k
        for i in range(1, n + 1):
            for comb in itertools.combinations_with_replacement(digits, i):
                if sum(int(x) for x in comb) % k == 0:
                    # Create a counter for the current combination
                    count = Counter(comb)
                    
                    # Calculate permutations of the combination
                    total_permutations = perm(count)
                    
                    # Add to good_count only if there is at least one digit that can be the center of a palindrome
                    if any(v % 2 == 1 for v in count.values()):
                        good_count += total_permutations
        
        return good_count