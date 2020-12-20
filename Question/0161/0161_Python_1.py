class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s1, s2 = len(s), len(t)

        if s1 == s2 == 0:
            return False

        if s1 == s2:
            differ = 0
            for i in range(s1):
                if s[i] != t[i]:
                    differ += 1
                    if differ > 1:
                        return False
            return differ == 1

        if s1 > s2:
            s, t = t, s
            s1, s2 = s2, s1

        if s1 == s2 - 1:
            i1, i2 = 0, 0
            differ = 0
            while i1 < s1 and i2 < s2:
                if s[i1] != t[i2]:
                    i2 += 1
                    differ += 1
                    if differ > 1:
                        return False
                else:
                    i1 += 1
                    i2 += 1
            if i1 == s1 and i2 == s2:
                return True
            elif differ == 0:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    print(Solution().isOneEditDistance(s="ab", t="acb"))  # True
    print(Solution().isOneEditDistance(s="ab", t="cab"))  # True
