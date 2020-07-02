class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().removeOuterParentheses("(()())(())"))  # "()()()"
    print(Solution().removeOuterParentheses("(()())(())(()(()))"))  # "()()()()(())"
    print(Solution().removeOuterParentheses("()()"))  # ""
