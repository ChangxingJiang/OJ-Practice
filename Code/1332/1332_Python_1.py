class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if "a" in s and "b" in s and s != s[::-1]:
            return 2
        elif len(s) > 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    print(Solution().removePalindromeSub(s="ababa"))  # 1
    print(Solution().removePalindromeSub(s="abb"))  # 2
    print(Solution().removePalindromeSub(s="baabb"))  # 2
    print(Solution().removePalindromeSub(s=""))  # 0
