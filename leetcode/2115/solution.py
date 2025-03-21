from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Create a graph where each ingredient points to the recipes that require it
        graph = defaultdict(list)
        # Create a dictionary to count the number of incoming edges (dependencies) for each recipe
        in_degree = {recipe: 0 for recipe in recipes}
        
        # Build the graph and in_degree map
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                if recipe in in_degree:
                    in_degree[recipe] += 1
        
        # Initialize a queue with all supplies (these have no dependencies)
        queue = deque(supplies)
        result = []
        
        # Process the queue
        while queue:
            supply = queue.popleft()
            for recipe in graph[supply]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        
        return result