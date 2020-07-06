from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        now = 1
        for n in nums:
            now += n
            if now < 1:
                ans += 1 - now
                now = 1
        return ans


if __name__ == "__main__":
    print(Solution().minStartValue(nums=[-3, 2, -3, 4, 2]))  # 5
    print(Solution().minStartValue(nums=[1, 2]))  # 1
    print(Solution().minStartValue(nums=[1, -2, -3]))  # 5
