from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -100000009
        prefix = 0
        for n in nums:
            prefix += n
            if prefix > ans:
                ans = prefix
            if prefix < 0:
                prefix = 0
        return ans


if __name__ == "__main__":
    # 6
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
