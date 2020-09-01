class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0

        # 正向遍历
        left = right = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
                if left == right:
                    ans = max(ans, right * 2)
                elif left < right:
                    left = 0
                    right = 0

        # 反向遍历
        left = right = 0
        for ch in s[::-1]:
            if ch == "(":
                left += 1
                if left == right:
                    ans = max(ans, left * 2)
                elif left > right:
                    left = 0
                    right = 0
            else:
                right += 1

        return ans


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))  # 2
    print(Solution().longestValidParentheses(")()())"))  # 4
    print(Solution().longestValidParentheses("()"))  # 2
    print(Solution().longestValidParentheses(")("))  # 0
    print(Solution().longestValidParentheses("()(()"))  # 2
    print(Solution().longestValidParentheses("()()"))  # 4
    print(Solution().longestValidParentheses("(()()"))  # 4
