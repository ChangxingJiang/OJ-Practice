import collections


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        for ch in s:
            count[ch] -= 1
            if ch not in stack:
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
        return "".join(stack)


if __name__ == "__main__":
    print(Solution().smallestSubsequence("cdadabcc"))  # "adbc"
    print(Solution().smallestSubsequence("abcd"))  # "abcd"
    print(Solution().smallestSubsequence("ecbacba"))  # "eacb"
    print(Solution().smallestSubsequence("leetcode"))  # "letcod"
