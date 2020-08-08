class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for ch in S:
            if ch == "c":
                if len(stack) < 2 or stack.pop() != "b" or stack.pop() != "a":
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("aabcbc"))  # True
    print(Solution().isValid("abcabcababcc"))  # True
    print(Solution().isValid("abccba"))  # False
    print(Solution().isValid("cababc"))  # False
