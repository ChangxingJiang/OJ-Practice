class Solution:
    def longestPrefix(self, s: str) -> str:
        lst = [0] * len(s)
        for i in range(1, len(s)):
            now = lst[i - 1]
            while now > 0 and s[now] != s[i]:
                now = lst[now - 1]
            if s[now] == s[i]:
                lst[i] = now + 1
        return s[:lst[-1]]


if __name__ == "__main__":
    print(Solution().longestPrefix(s="level"))  # "1"
    print(Solution().longestPrefix(s="ababab"))  # "abab"
    print(Solution().longestPrefix(s="leetcodeleet"))  # "leet"
    print(Solution().longestPrefix(s="a"))  # ""
