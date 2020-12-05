from typing import List


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        pass


if __name__ == "__main__":
    # "<b>abc</b>xyz<b>123</b>"
    print(Solution().addBoldTag(s="abcxyz123",
                                dict=["abc", "123"]))

    # "<b>aaabbc</b>c"
    print(Solution().addBoldTag(s="aaabbcc",
                                dict=["aaa", "aab", "bc"]))
