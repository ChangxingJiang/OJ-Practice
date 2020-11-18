from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        prefix = 0
        min_prefix = 0
        for n in nums:
            prefix += n
            if n > 0:
                ans = max(ans, prefix - min_prefix)
            else:
                min_prefix = min(min_prefix, prefix)
                ans = max(ans, n)
        return ans


if __name__ == "__main__":
    # 6
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
