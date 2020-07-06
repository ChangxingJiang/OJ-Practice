import collections
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        ans = -1
        for key, value in count.items():
            if key == value:
                ans = max(ans, key)
        return ans


if __name__ == "__main__":
    print(Solution().findLucky(arr=[2, 2, 3, 4]))  # 2
    print(Solution().findLucky(arr=[1, 2, 2, 3, 3, 3]))  # 3
    print(Solution().findLucky(arr=[2, 2, 2, 3, 3]))  # -1
    print(Solution().findLucky(arr=[5]))  # -1
    print(Solution().findLucky(arr=[7, 7, 7, 7, 7, 7, 7]))  # 7
