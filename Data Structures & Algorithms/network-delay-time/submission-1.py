class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        # generate each node with target and weight
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        # build default cost for each node, setting starting node at zero
        costs = {}
        for node in range(1, n + 1):
            costs[node] = float("inf")
        costs[k] = 0

        # Dijkstra
        processed = set()
        while len(processed) < n:
            lowest_cost = float("inf")
            lowest_cost_node = None

            # finding lowest cost node that is not processed
            for node in costs:
                cost = costs[node]

                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node

            # break since no more nodes
            if lowest_cost_node is None:
                break

            # neighbors check cost
            for neighbor, weight in graph.get(lowest_cost_node, []):
                new_cost = lowest_cost + weight
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
            
            # add to processed
            processed.add(lowest_cost_node)

        if any(cost == float("inf") for cost in costs.values()):
            return -1

        return max(costs.values())
