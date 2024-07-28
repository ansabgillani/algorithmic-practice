class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Function to calculate waiting time at a node based on the current time
        def wait_time(current_time):
            return ((current_time // change) + 1) * change - current_time

        # Priority queue: (time, node)
        pq = [(0, 1)]

        # Track minimum times to reach each node
        min_times = [float('inf')] * (n + 1)
        second_min_times = [float('inf')] * (n + 1)

        while pq:
            current_time, node = heappop(pq)

            # If the second minimum time is already found for this node, skip
            if second_min_times[node] != float('inf'):
                continue

            # Update min and second_min times for the current node
            if current_time < min_times[node]:
                min_times[node], second_min_times[node] = current_time, min_times[node]
            elif current_time < second_min_times[node]:
                second_min_times[node] = current_time

            # Explore neighbors
            for neighbor in graph[node]:
                next_time = current_time + time

                # Check if waiting is necessary at the neighbor
                if (next_time // change) % 2 == 1:
                    next_time += wait_time(next_time)

                heappush(pq, (next_time, neighbor))

        return second_min_times[n]