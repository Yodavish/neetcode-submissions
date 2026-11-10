class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v,w))
        
        costs = {}
        for node in range(1, n + 1):
            costs[node] = float("inf")
        costs[k] = 0

        processed = set()
        while len(processed) < n:
            lowest_cost = float("inf")
            lowest_cost_node = None

            for node in costs:
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = costs[node]
                    lowest_cost_node = node
            
            if lowest_cost_node is None:
                break

            for neighbor, weight in graph.get(lowest_cost_node, []):
                new_cost = weight + lowest_cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost

            processed.add(lowest_cost_node)
        
        if any(cost == float("inf") for cost in costs.values()):
            return -1

        return max(costs.values())