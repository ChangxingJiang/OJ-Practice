from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        now = float("-inf")  # 当前最大的1-3-2中的2
        stack = []  # 单调栈
        for n in reversed(nums):
            if n < now:
                return True
            while stack and stack[-1] < n:
                now = stack.pop()
            stack.append(n)
        return False


if __name__ == "__main__":
    print(Solution().find132pattern([1, 2, 3, 4]))  # False
    print(Solution().find132pattern([3, 1, 4, 2]))  # True
    print(Solution().find132pattern([-1, 3, 2, 0]))  # True
    print(Solution().find132pattern([5, 6, 4, 7, 3, 8, 2, 9, 1]))  # False
    print(Solution().find132pattern([1, 0, 1, -4, -3]))  # False
    print(Solution().find132pattern([-2, 1, -2]))  # False
