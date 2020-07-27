class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ")" and stack[-1] != "(":
                    return False
                elif c == "]" and stack[-1] != "[":
                    return False
                elif c == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("()"))  # True
    print(Solution().isValid("()[]{}"))  # True
    print(Solution().isValid("(]"))  # False
    print(Solution().isValid("([)]"))  # False
    print(Solution().isValid("{[]}"))  # True
    print(Solution().isValid("["))  # False
    print(Solution().isValid("]"))  # False
    print(Solution().isValid("(([]){})"))  # True
    print(Solution().isValid("[([]])"))  # False
