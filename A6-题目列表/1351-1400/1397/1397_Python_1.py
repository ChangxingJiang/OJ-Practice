class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().findGoodStrings(n=2, s1="aa", s2="da", evil="b"))  # 51
    print(Solution().findGoodStrings(n=8, s1="leetcode", s2="leetgoes", evil="leet"))  # 0
    print(Solution().findGoodStrings(n=2, s1="gx", s2="gz", evil="x"))  # 2
