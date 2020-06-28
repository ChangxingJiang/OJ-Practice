import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        else:
            return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar("aabb"))  # -1
    print(Solution().firstUniqChar("leetcode"))  # 0
    print(Solution().firstUniqChar("loveleetcode"))  # 2
