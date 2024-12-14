class Solution:
    def continuousSubarrays(self, nums):
        minq = deque()
        maxq = deque()

        result, left = 0, 0
        for right in range(len(nums)):
            while minq and nums[minq[-1]] > nums[right]:
                minq.pop()
            while maxq and nums[maxq[-1]] < nums[right]:
                maxq.pop()

            minq.append(right)
            maxq.append(right)

            if nums[maxq[0]] - nums[minq[0]] > 2:
                left += 1
                if left > minq[0]:
                    minq.popleft()
                if left > maxq[0]:
                    maxq.popleft()

            result += right - left + 1

        return result