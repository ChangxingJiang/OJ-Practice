from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if set(nums) == {1}:
            return len(nums) - 1

        ans = 0

        last, now = 0, 0
        for n in nums:
            if n == 1:
                now += 1
            else:
                ans = max(ans, last + now)
                last = now
                now = 0

        ans = max(ans, last + now)

        return ans


if __name__ == "__main__":
    print(Solution().longestSubarray(nums=[1, 1, 0, 1]))  # 3
    print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
    print(Solution().longestSubarray(nums=[1, 1, 1]))  # 2
    print(Solution().longestSubarray(nums=[1, 1, 0, 0, 1, 1, 1, 0, 1]))  # 4
    print(Solution().longestSubarray(nums=[0, 0, 0]))  # 0
