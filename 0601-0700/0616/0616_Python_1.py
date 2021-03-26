from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        size = len(s)
        mask = [False] * size
        for i in range(size):
            prefix = s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, i + len(word)):
                        mask[j] = True

        ans = []
        last = False
        for i, ch in enumerate(s):
            if last == False and mask[i] == True:
                ans.append("<b>")
                last = True
            elif last == True and mask[i] == False:
                ans.append("</b>")
                last = False
            ans.append(ch)
        if last:
            ans.append("</b>")

        return "".join(ans)


if __name__ == "__main__":
    # "<b>abc</b>xyz<b>123</b>"
    print(Solution().addBoldTag(s="abcxyz123", words=["abc", "123"]))

    # "<b>aaabbc</b>c"
    print(Solution().addBoldTag(s="aaabbcc", words=["aaa", "aab", "bc"]))
