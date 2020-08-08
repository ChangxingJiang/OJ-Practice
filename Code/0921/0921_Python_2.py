class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch == "(":
                stack.append(ch)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)


if __name__ == "__main__":
    print(Solution().minAddToMakeValid("())"))  # 1
    print(Solution().minAddToMakeValid("((("))  # 3
    print(Solution().minAddToMakeValid("()"))  # 0
    print(Solution().minAddToMakeValid("()))(("))  # 4
    print(Solution().minAddToMakeValid("(()("))  # 2
    print(Solution().minAddToMakeValid("((())"))  # 1
