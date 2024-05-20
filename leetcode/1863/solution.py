class Solution:
    def subset_xor_sum(self, nums):
        total_sum = 0
        n = len(nums)

        # Calculate XOR for each subset and sum them up
        for r in range(n + 1):
            for subset in self.combinations(nums, r):
                total_sum += self.reduce(lambda x, y: x ^ y, subset)

        return total_sum

    def combinations(self, iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)

    def reduce(self, function, iterable, initializer=None):
        it = iter(iterable)
        if initializer is None:
            try:
                accumulator = next(it)
            except StopIteration:
                raise TypeError('reduce() of empty sequence with no initial value')
        else:
            accumulator = initializer
        for x in it:
            accumulator = function(accumulator, x)
        return accumulator