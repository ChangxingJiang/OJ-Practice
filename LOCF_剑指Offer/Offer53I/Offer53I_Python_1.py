from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)


if __name__ == "__main__":
    print(Solution().search([5, 7, 7, 8, 8, 0], 8))  # 2
    print(Solution().search([5, 7, 7, 8, 8, 0], 6))  # 0
