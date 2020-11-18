from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            stack.append(n)
            ans += len(stack)
        return ans


if __name__ == "__main__":
    print(Solution().validSubarrays([1, 4, 2, 5, 3]))  # 11
    print(Solution().validSubarrays([3, 2, 1]))  # 3
    print(Solution().validSubarrays([2, 2, 2]))  # 6
