class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack or abs(ord(stack[-1]) - ord(ch)) != 32:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().makeGood(s="leEeetcode"))  # "leetcode"
    print(Solution().makeGood(s="abBAcC"))  # ""
    print(Solution().makeGood(s="s"))  # "s"
