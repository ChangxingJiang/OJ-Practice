class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().equalSubstring(s="abcd", t="bcdf", maxCost=3))  # 3
    print(Solution().equalSubstring(s="abcd", t="cdef", maxCost=3))  # 1
    print(Solution().equalSubstring(s="abcd", t="acde", maxCost=0))  # 1
