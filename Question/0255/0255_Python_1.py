from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        find = float("-inf")
        stack = []
        for n in preorder:
            if n < find:
                return False
            elif not stack or n < stack[-1]:
                stack.append(n)
            else:
                while stack and n > stack[-1]:
                    find = max(find, stack.pop())
                stack.append(n)
        return True


if __name__ == "__main__":
    print(Solution().verifyPreorder([5, 2, 6, 1, 3]))  # False
    print(Solution().verifyPreorder([5, 2, 1, 3, 6]))  # True
