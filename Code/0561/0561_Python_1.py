from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


if __name__ == "__main__":
    print(Solution().arrayPairSum([1, 4, 3, 2]))  # 4
