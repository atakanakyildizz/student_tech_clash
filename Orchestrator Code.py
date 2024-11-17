from typing import List, Dict, Any
import heapq

class Orchestrator:
    def __init__(self):
        self.requests = []  # Storage for travel requests

    def receive_data(self, travel_data: Dict[str, Any]):
        """
        Receives travel data from user agents.
        """
        self.requests.append(travel_data)
        print(f"Received travel data: {travel_data}")

    def calculate_routes(self):
        """
        Process travel data and calculate optimized routes.
        """
        print("Calculating routes based on the dataset...")
        
        # Example: Using Dijkstra's algorithm to find the shortest path
        # This is a simplified example and assumes a predefined graph of locations
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

        def dijkstra(graph, start, end):
            queue = [(0, start, [])]
            seen = set()
            min_dist = {start: 0}
            while queue:
                (cost, node, path) = heapq.heappop(queue)
                if node in seen:
                    continue
                seen.add(node)
                path = path + [node]
                if node == end:
                    return (cost, path)
                for next_node, weight in graph.get(node, {}).items():
                    if next_node in seen:
                        continue
                    prev = min_dist.get(next_node, None)
                    next_cost = cost + weight
                    if prev is None or next_cost < prev:
                        min_dist[next_node] = next_cost
                        heapq.heappush(queue, (next_cost, next_node, path))
            return float("inf"), []

        routes = []
        for request in self.requests:
            start, end = request['request'].split(' to ')
            cost, path = dijkstra(graph, start, end)
            routes.append({"user_id": request["user_id"], "route": path, "cost": cost})

        print(f"Calculated Routes: {routes}")
        return routes

# Example usage
if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.receive_data({"user_id": "user1", "request": "A to D"})
    orchestrator.receive_data({"user_id": "user2", "request": "B to C"})
    orchestrator.calculate_routes()