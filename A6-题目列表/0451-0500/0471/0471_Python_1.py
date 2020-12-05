class Solution:
    def encode(self, s: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().encode(s="aaa"))  # "aaa"
    print(Solution().encode(s="aaaaa"))  # "5[a]"
    print(Solution().encode(s="aaaaaaaaaa"))  # "10[a]"
    print(Solution().encode(s="aabcaabcd"))  # "2[aabc]d"
    print(Solution().encode(s="abbbabbbcabbbabbbc"))  # "2[2[abbb]c]"
