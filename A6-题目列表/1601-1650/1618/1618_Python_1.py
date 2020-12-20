from typing import List


# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
class FontInfo(object):
    def getWidth(self, fontSize, ch):
        """
        :type fontSize: int
        :type ch: char
        :rtype int
        """

    def getHeight(self, fontSize):
        """
        :type fontSize: int
        :rtype int
        """


class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        pass


if __name__ == "__main__":
    pass
