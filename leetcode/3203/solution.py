from collections import defaultdict, deque

def min_diameter_after_merging(edges1, edges2):
    def bfs_max_path(graph, start):
        visited = [False] * len(graph)
        queue = deque([(start, 0)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if not visited[node]:
                visited[node] = True
                for neighbor in graph[node]:
                    queue.append((neighbor, depth + 1))
                    max_depth = max(max_depth, depth + 1)
        return max_depth

    def find_lca(graph, u, v):
        def dfs(node, parent):
            if node == u or node == v:
                nodes.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, node)

        lca = None
        while u != v:
            if len(nodes & set(graph[u])) > 0:
                u, lca = lca, u
            else:
                u, lca = lca, v
            nodes.discard(u)
            nodes.discard(v)
        return lca

    def connect_nodes(graph1, graph2, root1, root2):
        visited = set()
        queue = deque([(root1, 0)])
        while queue:
            node, depth = queue.popleft()
            if node in graph2 and node not in visited:
                visited.add(node)
                return depth
            for neighbor in graph1[node]:
                if neighbor != root1 and neighbor not in visited:
                    queue.append((neighbor, depth + 1))
        return -1

    # Build the graphs
    n = len(edges1) + 1
    m = len(edges2) + 1
    graph1 = defaultdict(list)
    graph2 = defaultdict(list)

    for u, v in edges1:
        graph1[u].append(v)
        graph1[v].append(u)

    for u, v in edges2:
        graph2[u].append(v)
        graph2[v].append(u)

    # Find the maximum path length of each tree
    root1 = 0
    max_path1 = bfs_max_path(graph1, root1)

    root2 = 0
    max_path2 = bfs_max_path(graph2, root2)

    # Find the lowest common ancestor (LCA) of the two trees
    lca = find_lca(graph1 | graph2, root1, root2)

    # Connect the LCA from both trees and calculate the new diameter
    connect_depth = connect_nodes(graph1, graph2, lca, lca)
    
    # Calculate the minimum possible diameter after merging
    min_diameter = max(max_path1, max_path2) + 2 * connect_depth

    return min_diameter - 1 if min_diameter % 2 == 0 else min_diameter