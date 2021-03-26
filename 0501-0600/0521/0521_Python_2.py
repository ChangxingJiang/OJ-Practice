class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1


if __name__ == "__main__":
    print(Solution().findLUSlength("aba", "cdc"))  # 3
    print(Solution().findLUSlength("aaa", "bbb"))  # 3
    print(Solution().findLUSlength("aaa", "aaa"))  # -1
    print(Solution().findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))  # 17
