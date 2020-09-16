import re


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        S, num = re.subn(r"\((?=.*?)\)", "", S)
        while num > 0:
            S, num = re.subn(r"\((?=.*?)\)", "", S)
        return len(S)


if __name__ == "__main__":
    print(Solution().minAddToMakeValid("())"))  # 1
    print(Solution().minAddToMakeValid("((("))  # 3
    print(Solution().minAddToMakeValid("()"))  # 0
    print(Solution().minAddToMakeValid("()))(("))  # 4
    print(Solution().minAddToMakeValid("(()("))  # 2
    print(Solution().minAddToMakeValid("((())"))  # 1
