class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if len(stack) > 1:
                    stack.pop()
                    ans = max(ans, i - stack[-1])
                else:
                    stack[-1] = i
        return ans


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))  # 2
    print(Solution().longestValidParentheses(")()())"))  # 4
    print(Solution().longestValidParentheses("()"))  # 2
    print(Solution().longestValidParentheses(")("))  # 0
    print(Solution().longestValidParentheses("()(()"))  # 2
    print(Solution().longestValidParentheses("()()"))  # 4
    print(Solution().longestValidParentheses("(()()"))  # 4
