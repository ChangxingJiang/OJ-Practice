class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        diff = -1
        already = False
        for i in range(size):
            if s1[i] != s2[i]:
                if already:
                    return False
                if diff == -1:
                    diff = i
                else:
                    if not (s1[diff] == s2[i] and s2[diff] == s1[i]):
                        return False
                    else:
                        already = True
        return diff == -1 or already is True


if __name__ == "__main__":
    print(Solution().areAlmostEqual(s1="bank", s2="kanb"))  # True
    print(Solution().areAlmostEqual(s1="attack", s2="defend"))  # False
    print(Solution().areAlmostEqual(s1="kelb", s2="kelb"))  # True
    print(Solution().areAlmostEqual(s1="abcd", s2="dcba"))  # False
    print(Solution().areAlmostEqual(s1="aa", s2="ac"))  # False
    print(Solution().areAlmostEqual(s1="qgqeg", s2="gqgeq"))  # False
