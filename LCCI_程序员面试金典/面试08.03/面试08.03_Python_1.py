from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == n:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().findMagicIndex([0, 2, 3, 4, 5]))  # 0
    print(Solution().findMagicIndex([1, 1, 1]))  # 1
