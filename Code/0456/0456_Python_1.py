from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        now = None
        for n in nums:
            for s in stack:
                if s[0] < n < s[1]:
                    return True

            if now is None:
                now = n
            elif n < now:
                now = n
            elif n > now:
                for i in range(len(stack) - 1, -1, -1):
                    s = stack[i]
                    if now <= s[0] < s[1] <= n:
                        stack.pop(i)
                stack.append([now, n])

        return False


if __name__ == "__main__":
    print(Solution().find132pattern([1, 2, 3, 4]))  # False
    print(Solution().find132pattern([3, 1, 4, 2]))  # True
    print(Solution().find132pattern([-1, 3, 2, 0]))  # True
    print(Solution().find132pattern([5, 6, 4, 7, 3, 8, 2, 9, 1]))  # False
    print(Solution().find132pattern([1, 0, 1, -4, -3]))  # False
