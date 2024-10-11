class Solution:
    def smallestChair(self, times, targetFriend):
        times.sort()
        occupied = []
        free_chairs = []

        for i, (arrival, leaving) in enumerate(times):
            while occupied and occupied[0][0] <= arrival:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(free_chairs, chair)

            if not free_chairs:
                chair = len(free_chairs)
            else:
                chair = heapq.heappop(free_chairs)

            heapq.heappush(occupied, (leaving, chair))

            if i == targetFriend:
                return chair

        return -1