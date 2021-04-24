from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        min_val = 0
        max_val = 0
        now = 0
        for num in nums:
            now += num
            ans = max(ans, now - min_val, max_val - now)
            if now < min_val:
                min_val = now
            if now > max_val:
                max_val = now

        return ans


if __name__ == "__main__":
    print(Solution().maxAbsoluteSum([1, -3, 2, 3, -4]))  # 5
    print(Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # 8
