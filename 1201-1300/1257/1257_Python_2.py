from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for region in reversed(regions):
            if region1 in region:
                region1 = region[0]
            if region2 in region:
                region2 = region[0]
            if region1 == region2:
                return region1


if __name__ == "__main__":
    # "North America"
    print(Solution().findSmallestRegion(regions=[["Earth", "North America", "South America"],
                                                 ["North America", "United States", "Canada"],
                                                 ["United States", "New York", "Boston"],
                                                 ["Canada", "Ontario", "Quebec"],
                                                 ["South America", "Brazil"]],
                                        region1="Quebec",
                                        region2="New York"))
