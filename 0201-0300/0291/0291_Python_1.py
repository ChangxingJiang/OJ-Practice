class Solution:
    def __init__(self):
        self.dic1 = {}  # 从pattern到s的映射
        self.dic2 = {}  # 从s到pattern的映射

    def wordPatternMatch(self, pattern: str, s: str, i1=0, i2=0) -> bool:
        if i1 == len(pattern) and i2 == len(s):
            return True
        elif i1 == len(pattern):
            return False
        elif pattern[i1] in self.dic1:
            ch = self.dic1[pattern[i1]]
            size = len(ch)
            if len(s) - i2 >= size and ch == s[i2:i2 + size]:
                return self.wordPatternMatch(pattern, s, i1 + 1, i2 + size)
            else:
                return False
        else:
            for i in range(1, len(s) - i2 + 1):
                p = pattern[i1]
                ch = s[i2:i2 + i]

                if ch in self.dic2:
                    continue

                self.dic1[p] = ch
                self.dic2[ch] = p
                if self.wordPatternMatch(pattern, s, i1 + 1, i2 + i):
                    return True
                del self.dic1[p]
                del self.dic2[ch]
            return False


if __name__ == "__main__":
    print(Solution().wordPatternMatch(pattern="abab", s="redblueredblue"))  # True
    print(Solution().wordPatternMatch(pattern="aaaa", s="asdasdasdasd"))  # True
    print(Solution().wordPatternMatch(pattern="abab", s="asdasdasdasd"))  # True
    print(Solution().wordPatternMatch(pattern="aabb", s="xyzabcxzyabc"))  # False
    print(Solution().wordPatternMatch(pattern="d", s="e"))  # True
    print(Solution().wordPatternMatch(pattern="p", s=""))  # False
    print(Solution().wordPatternMatch(pattern="ab", s="aa"))  # False
