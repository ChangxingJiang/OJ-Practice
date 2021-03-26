from typing import List


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minBuildTime(blocks=[1], split=1))  # 1
    print(Solution().minBuildTime(blocks=[1, 2], split=5))  # 7
    print(Solution().minBuildTime(blocks=[1, 2, 3], split=1))  # 4
