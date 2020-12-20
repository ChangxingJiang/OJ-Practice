import functools


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @functools.lru_cache(None)
        def dfs(used, need):
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    if need <= i + 1 or not dfs(cur | used, need - i - 1):
                        return True
            return False

        return dfs(0, desiredTotal)


if __name__ == "__main__":
    print(Solution().canIWin(10, 11))  # False
    print(Solution().canIWin(10, 0))  # True
    print(Solution().canIWin(10, 40))  # False
    print(Solution().canIWin(5, 50))  # False
