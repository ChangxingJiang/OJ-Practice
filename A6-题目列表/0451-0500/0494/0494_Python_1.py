from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort(reverse=True)

        # 计算后缀和
        last = 0
        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            last += nums[i]
            suffix[i] = last

        def dfs(idx, now):
            if idx == len(nums):
                return 1 if now == S else 0
            if (S - now) > suffix[idx]:
                return 0
            else:
                return dfs(idx + 1, now + nums[idx]) + dfs(idx + 1, now - nums[idx])

        return dfs(0, 0)


if __name__ == "__main__":
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))  # 5
