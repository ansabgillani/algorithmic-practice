class Solution:
    def specialArrayII(self, nums, queries):
        prefix_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix_sum[i+1] = prefix_sum[i] ^ (num % 2)

        answer = []
        for q in queries:
            start, end = q
            if prefix_sum[start] != prefix_sum[end + 1]:
                answer.append(True)
            else:
                answer.append(False)

        return answer