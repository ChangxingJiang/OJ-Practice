from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(now, left, right):
            if len(now) == 2 * n:
                ans.append("".join(now))
                return
            if left < n:
                now.append("(")
                backtrack(now, left + 1, right)
                now.pop()
            if left > right:
                now.append(")")
                backtrack(now, left, right + 1)
                now.pop()

        ans = []
        backtrack([], 0, 0)
        return ans


if __name__ == "__main__":
    # [
    #     "((()))",
    #     "(()())",
    #     "(())()",
    #     "()(())",
    #     "()()()"
    # ]
    print(Solution().generateParenthesis(3))
