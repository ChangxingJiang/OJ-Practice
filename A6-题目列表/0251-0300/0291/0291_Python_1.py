class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().wordPatternMatch(pattern="abab", s="redblueredblue"))  # True
    print(Solution().wordPatternMatch(pattern="aaaa", s="asdasdasdasd"))  # True
    print(Solution().wordPatternMatch(pattern="abab", s="asdasdasdasd"))  # True
    print(Solution().wordPatternMatch(pattern="aabb", s="xyzabcxzyabc"))  # False
