from functools import lru_cache


class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == "+" and s[i + 1] == "+":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False


if __name__ == "__main__":
    print(Solution().canWin("++++"))  # True
    print(Solution().canWin("++++++"))  # True
    print(Solution().canWin("+++++++++"))  # False
