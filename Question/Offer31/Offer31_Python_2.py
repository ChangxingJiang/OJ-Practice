from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return not stack


if __name__ == "__main__":
    # True
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))

    # False
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
