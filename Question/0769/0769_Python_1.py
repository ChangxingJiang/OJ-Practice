from typing import List


class Solution:
    def maxChunksToSorted(self, arr1: List[int]) -> int:
        ans = 0
        find = set()
        need = set()
        for i in range(len(arr1)):
            find.add(arr1[i])
            need.add(i)
            if find == need:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().maxChunksToSorted(arr1=[4, 3, 2, 1, 0]))  # 1
    print(Solution().maxChunksToSorted(arr1=[1, 0, 2, 3, 4]))  # 4
    print(Solution().maxChunksToSorted(arr1=[0, 2, 1, 4, 3]))  # 3
