from typing import List


class Solution:
    def generateParenthesis(self, n: int, left: int = 0) -> List[str]:
        self.now = []
        self.ans = []

        def count(l, r):
            if l == r:
                self.now.append("(")
                count(l + 1, r)
                self.now.pop()
            elif l == n:
                self.ans.append("".join(self.now + [")"] * (l - r)))
            else:
                self.now.append("(")
                count(l + 1, r)
                self.now.pop()
                self.now.append(")")
                count(l, r + 1)
                self.now.pop()

        count(l=0, r=0)

        return self.ans


if __name__ == "__main__":
    # [
    #   "((()))",
    #   "(()())",
    #   "(())()",
    #   "()(())",
    #   "()()()"
    # ]
    print(Solution().generateParenthesis(3))
