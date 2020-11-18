from typing import List


class Solution:
    def __init__(self):
        self.hashmap = {}
        self.ans = None

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for region in regions:
            self.hashmap[region[0]] = region[1:]

        self.dfs(regions[0][0], region1, region2)
        return self.ans

    def dfs(self, p, r1, r2):
        find = 0
        if p == r1 or p == r2:
            find += 1
        if p in self.hashmap:
            find += sum(self.dfs(c, r1, r2) for c in self.hashmap[p])
        if find == 2:
            if not self.ans:
                self.ans = p
        return find


if __name__ == "__main__":
    # "North America"
    print(Solution().findSmallestRegion(regions=[["Earth", "North America", "South America"],
                                                 ["North America", "United States", "Canada"],
                                                 ["United States", "New York", "Boston"],
                                                 ["Canada", "Ontario", "Quebec"],
                                                 ["South America", "Brazil"]],
                                        region1="Quebec",
                                        region2="New York"))
