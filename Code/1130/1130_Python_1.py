from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        for n in arr:
            if not stack or stack[-1] > n:
                stack.append(n)
            else:
                while stack:
                    top = stack.pop()
                    if stack and stack[-1] <= n:
                        ans += top * stack[-1]
                    else:
                        ans += top * n
                        stack.append(n)
                        break
        while len(stack) > 1:
            ans += stack.pop() * stack[-1]
        return ans


if __name__ == "__main__":
    print(Solution().mctFromLeafValues([6, 2, 4]))  # 32
    print(Solution().mctFromLeafValues([7, 12, 8, 10]))  # 284
    print(Solution().mctFromLeafValues([15, 13, 5, 3, 15]))  # 500
