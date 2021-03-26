import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        size = len(s)
        left, right = 0, 0
        count = collections.Counter()
        while right < size:
            ch1 = s[right]
            count[ch1] += 1
            while len(count) > k:
                ch2 = s[left]
                count[ch2] -= 1
                if count[ch2] == 0:
                    del count[ch2]
                left += 1
            right += 1
            ans = max(ans, right - left)
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringKDistinct(s="eceba", k=2))  # 3
    print(Solution().lengthOfLongestSubstringKDistinct(s="aa", k=1))  # 2
