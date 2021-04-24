class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            new = left
            while new <= right and s[left] == s[new]:
                new += 1
            left = new

            new = right
            while new >= left and s[right] == s[new]:
                new -= 1
            right = new

        return right - left + 1


if __name__ == "__main__":
    print(Solution().minimumLength("ca"))  # 2
    print(Solution().minimumLength("cabaabac"))  # 0
    print(Solution().minimumLength("aabccabba"))  # 3

    # 自制测试用例
    print(Solution().minimumLength("a"))  # 1
