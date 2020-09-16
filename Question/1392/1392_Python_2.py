class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        lst = [0] * N
        i, j = 1, 0
        while i < N:
            if s[i] == s[j]:
                j += 1
                lst[i] = j
                i += 1
            elif j > 0:
                j = lst[j - 1]
            else:
                i += 1
        return s[:lst[-1]]


if __name__ == "__main__":
    print(Solution().longestPrefix(s="level"))  # "1"
    print(Solution().longestPrefix(s="ababab"))  # "abab"
    print(Solution().longestPrefix(s="leetcodeleet"))  # "leet"
    print(Solution().longestPrefix(s="a"))  # ""
