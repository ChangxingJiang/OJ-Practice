import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = collections.Counter(s1), collections.Counter()
        count = 0

        i1 = i2 = 0
        while i2 < len(s2):
            ch2 = s2[i2]
            i2 += 1

            if ch2 in need:
                window[ch2] += 1
                if window[ch2] == need[ch2]:
                    count += 1

            while i2 - i1 >= len(s1):
                if count == len(need):
                    return True

                ch1 = s2[i1]
                i1 += 1

                if ch1 in window:
                    if window[ch1] == need[ch1]:
                        count -= 1
                    window[ch1] -= 1

        return False


if __name__ == "__main__":
    print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))  # True
    print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))  # False
