import functools


class Solution:
    @functools.lru_cache(None)
    def countVowelStrings(self, n: int, t=5) -> int:
        if t == 0:
            return 0
        if n == 1:
            return t

        ans = 0
        for i in range(1, t + 1):
            ans += self.countVowelStrings(n - 1, i)
        return ans


if __name__ == "__main__":
    print(Solution().countVowelStrings(1))  # 5
    print(Solution().countVowelStrings(2))  # 15
    print(Solution().countVowelStrings(33))  # 66045
