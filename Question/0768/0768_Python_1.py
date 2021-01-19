import collections
from typing import List


class Solution:
    def maxChunksToSorted(self, arr1: List[int]) -> int:
        arr2 = list(arr1)
        arr2.sort()
        ans = 0
        count = collections.Counter()
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                count[arr1[i]] += 1
                count[arr2[i]] -= 1
                if count[arr1[i]] == 0:
                    count.pop(arr1[i])
                if count[arr2[i]] == 0:
                    count.pop(arr2[i])
            if len(count) == 0:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().maxChunksToSorted(arr1=[5, 4, 3, 2, 1]))  # 1
    print(Solution().maxChunksToSorted(arr1=[2, 1, 3, 4, 4]))  # 4
