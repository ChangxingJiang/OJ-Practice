from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        for ch in s:
            count[ch] -= 1
            if ch not in stack:
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("bcabc"))  # "abc"
    print(Solution().removeDuplicateLetters("cbacdcbc"))  # "acdb"
    print(Solution().removeDuplicateLetters("abacb"))  # "abc"
