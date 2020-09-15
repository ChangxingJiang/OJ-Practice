from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            ans = {"()"}
            for _ in range(n - 1):
                now = set()
                for p in ans:
                    for i in range(len(p)):
                        now.add(p[:i] + "()" + p[i:])
                ans = now
        return list(ans)


if __name__ == "__main__":
    # [
    #     "((()))",
    #     "(()())",
    #     "(())()",
    #     "()(())",
    #     "()()()"
    # ]
    print(Solution().generateParenthesis(3))
