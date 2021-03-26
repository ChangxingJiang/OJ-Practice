from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = len(nums) + 1

        now = 0
        i1 = 0
        for i2 in range(len(nums)):
            now += nums[i2]
            while now - nums[i1] >= s:
                now -= nums[i1]
                i1 += 1
            if now >= s:
                ans = min(ans, i2 - i1 + 1)

        return ans if ans <= len(nums) else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))  # 2
