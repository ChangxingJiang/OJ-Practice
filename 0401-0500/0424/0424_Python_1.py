import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        left = right = 0

        ans = 0

        while right < len(s):
            count[s[right]] += 1
            ans = max(ans, count[s[right]])

            # 窗口长度增长之后不会减少，一直保留最大值时的情况
            if (right - left + 1) - ans > k:
                count[s[left]] -= 1
                left += 1
            right += 1

        return right - left


if __name__ == "__main__":
    print(Solution().characterReplacement(s="ABAB", k=2))  # 4
    print(Solution().characterReplacement(s="AABABBA", k=1))  # 4
