class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        ans = ""
        for s in S:
            if s == "(":
                count += 1
                if count > 1:
                    ans += s
            else:
                count -= 1
                if count > 0:
                    ans += s
        return ans


if __name__ == "__main__":
    print(Solution().removeOuterParentheses("(()())(())"))  # "()()()"
    print(Solution().removeOuterParentheses("(()())(())(()(()))"))  # "()()()()(())"
    print(Solution().removeOuterParentheses("()()"))  # ""
