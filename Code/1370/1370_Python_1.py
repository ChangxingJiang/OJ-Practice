import collections


class Solution:
    def sortString(self, s: str) -> str:
        count = collections.Counter(s)
        ans = ""
        while len(ans) < len(s):
            sub = ""
            for k in list("abcdefghijklmnopqrstuvwxyz"):
                if count[k] > 0:
                    sub += k
                    count[k] -= 1
            ans += sub
            sub = ""
            for k in list("zyxwvutsrqponmlkjihgfedcba"):
                if count[k] > 0:
                    sub += k
                    count[k] -= 1
            ans += sub
        return ans


if __name__ == "__main__":
    print(Solution().sortString("aaaabbbbcccc"))  # abccbaabccba
    print(Solution().sortString("rat"))  # art
    print(Solution().sortString("leetcode"))  # cdelotee
    print(Solution().sortString("ggggggg"))  # ggggggg
    print(Solution().sortString("spo"))  # ops
