from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        g = [0] * (len(nums) + 1)
        for n in nums:
            g[n] = 1
        ans = []
        for n in range(1, len(nums) + 1):
            if g[n] == 0:
                ans.append(n)
        return ans


if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5,6]
    print(Solution().findDisappearedNumbers([]))  # []
    print(Solution().findDisappearedNumbers([1, 1]))  # [2]
