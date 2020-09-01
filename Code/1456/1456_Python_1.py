class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 处理字符串过短的情况
        if len(s) <= k:
            return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

        # 滑动窗口处理其他情况
        ans = num = s[:k].count("a") + s[:k].count("e") + s[:k].count("i") + s[:k].count("o") + s[:k].count("u")
        for i in range(len(s) - k):
            if s[i] in {"a", "e", "i", "o", "u"}:
                num -= 1
            if s[i + k] in {"a", "e", "i", "o", "u"}:
                num += 1
                ans = max(num, ans)
        return ans


if __name__ == "__main__":
    print(Solution().maxVowels(s="abciiidef", k=3))  # 3
    print(Solution().maxVowels(s="aeiou", k=2))  # 2
    print(Solution().maxVowels(s="leetcode", k=3))  # 2
    print(Solution().maxVowels(s="rhythms", k=4))  # 0
    print(Solution().maxVowels(s="tryhard", k=4))  # 1
