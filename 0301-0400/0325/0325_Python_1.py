from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        last = 0
        ans = 0
        count = {}
        for i in range(len(nums)):
            if last not in count:
                count[last] = i
            last += nums[i]
            aim = last - k
            if aim in count:
                ans = max(ans, i - count[aim] + 1)
        return ans


if __name__ == "__main__":
    # 4
    print(Solution().maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))

    # 2
    print(Solution().maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
