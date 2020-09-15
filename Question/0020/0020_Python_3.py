class Solution:
    def isValid(self, s: str) -> bool:
        last = len(s)
        new = 0
        while last != new:
            last = len(s)
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            new = len(s)
        return new == 0


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
