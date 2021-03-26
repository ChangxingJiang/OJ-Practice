from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        min_val = 0
        last = 0
        for n in nums:
            min_val = min(last, min_val)
            last += n
            ans = max(ans, last - min_val)
        return ans


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(Solution().maxSubArray([1]))  # 1
    print(Solution().maxSubArray([-1]))  # -1
    print(Solution().maxSubArray([-2, -1]))  # -1
    print(Solution().maxSubArray([1, 2]))  # 3
