from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

    # ["JFK","ATL","JFK","SFO","ATL","SFO"] & ["JFK","SFO","ATL","JFK","ATL","SFO"]
    print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
