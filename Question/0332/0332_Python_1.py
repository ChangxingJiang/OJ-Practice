import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for city1, city2 in tickets:
            graph[city1].append(city2)
        for city in graph:
            heapq.heapify(graph[city])

        def dfs(c1):
            while graph[c1]:
                c2 = heapq.heappop(graph[c1])
                dfs(c2)
            stack.append(c1)

        stack = []
        dfs("JFK")
        return stack[::-1]


if __name__ == "__main__":
    # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

    # ["JFK","ATL","JFK","SFO","ATL","SFO"] & ["JFK","SFO","ATL","JFK","ATL","SFO"]
    print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
