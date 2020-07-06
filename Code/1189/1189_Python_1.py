import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = collections.Counter(text)
        if "b" not in count or "a" not in count or "l" not in count or "o" not in count or "n" not in count:
            return 0
        else:
            return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])


if __name__ == "__main__":
    print(Solution().maxNumberOfBalloons("nlaebolko"))  # 1
    print(Solution().maxNumberOfBalloons("loonbalxballpoon"))  # 2
    print(Solution().maxNumberOfBalloons("leetcode"))  # 0
