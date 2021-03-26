import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for ch in s:
            if ch in dic:
                dic[ch] = False
            else:
                dic[ch] = True

        for ch, val in dic.items():
            if val:
                return ch

        return " "


if __name__ == "__main__":
    print(Solution().firstUniqChar("abaccdeff"))  # "b"
    print(Solution().firstUniqChar(""))  # " "
    print(Solution().firstUniqChar("leetcode"))  # "l"
