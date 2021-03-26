from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = 0
        now = 0
        for n in nums:
            now += n
            minimum = min(minimum, now)
        return 1 - minimum


if __name__ == "__main__":
    print(Solution().minStartValue(nums=[-3, 2, -3, 4, 2]))  # 5
    print(Solution().minStartValue(nums=[1, 2]))  # 1
    print(Solution().minStartValue(nums=[1, -2, -3]))  # 5
