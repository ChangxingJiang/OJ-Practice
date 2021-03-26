from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        size = len(pushed)
        idx = 0
        for elem in popped:
            if stack and stack[-1] == elem:
                stack.pop()
            else:
                while idx < size and pushed[idx] != elem:
                    stack.append(pushed[idx])
                    idx += 1
                if idx >= size:
                    return False
                else:
                    idx += 1
        return True


if __name__ == "__main__":
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))  # True
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))  # False
