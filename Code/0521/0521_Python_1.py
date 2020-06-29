class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) < len(b):
            a, b = b, a
        for size in range(len(a) - 1, -1, -1):
            for i in range(len(a) - size):
                s = a[i:]
                if s not in b:
                    return size + 1
        return -1


if __name__ == "__main__":
    print(Solution().findLUSlength("aba", "cdc"))  # 3
    print(Solution().findLUSlength("aaa", "bbb"))  # 3
    print(Solution().findLUSlength("aaa", "aaa"))  # -1
    print(Solution().findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))  # 17
