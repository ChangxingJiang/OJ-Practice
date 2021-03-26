import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        size = len(s)
        left, right = 0, 0
        count = collections.Counter()
        while right < size:
            ch1 = s[right]
            count[ch1] += 1
            while len(count) > 2:
                ch2 = s[left]
                count[ch2] -= 1
                if count[ch2] == 0:
                    del count[ch2]
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans


if __name__ == "__main__":
    # 3
    print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))

    # 5
    print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))

    # 5
    print(Solution().lengthOfLongestSubstringTwoDistinct("abcabcabc"))
