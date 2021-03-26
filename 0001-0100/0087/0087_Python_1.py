import functools


class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == "__main__":
    print(Solution().isScramble(s1="great", s2="rgeat"))  # True
    print(Solution().isScramble(s1="abcde", s2="caebd"))  # False
    print(Solution().isScramble(s1="greet", s2="egtre"))  # False
    print(Solution().isScramble(s1="geeet", s2="egtee"))  # True
    print(Solution().isScramble(s1="abcde", s2="baced"))  # True
    print(Solution().isScramble(s1="123456789", s2="215349867"))  # True
    print(Solution().isScramble(s1="ab", s2="aa"))  # False
    print(Solution().isScramble(s1="abb", s2="bba"))  # True
