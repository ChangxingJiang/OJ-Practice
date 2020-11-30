from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        pass


if __name__ == "__main__":
    # ["()()()", "(())()"]
    print(Solution().removeInvalidParentheses("()())()"))

    # ["(a)()()", "(a())()"]
    print(Solution().removeInvalidParentheses("(a)())()"))

    # [""]
    print(Solution().removeInvalidParentheses(")("))
