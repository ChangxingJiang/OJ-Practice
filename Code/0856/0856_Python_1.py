class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                now = 0
                while stack and stack[-1] != "(":
                    now += stack.pop()
                stack.pop()
                stack.append(now * 2 if now else 1)
        return sum(stack)


if __name__ == "__main__":
    print(Solution().scoreOfParentheses("()"))  # 1
    print(Solution().scoreOfParentheses("(())"))  # 2
    print(Solution().scoreOfParentheses("()()"))  # 2
    print(Solution().scoreOfParentheses("(()(()))"))  # 6
