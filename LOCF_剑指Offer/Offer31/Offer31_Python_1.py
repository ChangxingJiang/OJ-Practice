from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N1 = len(pushed)
        N2 = len(popped)
        stack = []
        idx1 = 0
        idx2 = 0
        while idx1 < N1 or idx2 < N2:
            if stack and stack[-1] == popped[idx2]:
                stack.pop()
                idx2 += 1
            else:
                if idx1 < N1:
                    stack.append(pushed[idx1])
                    idx1 += 1
                else:
                    return False
        return not stack


if __name__ == "__main__":
    # True
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))

    # False
    print(Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
