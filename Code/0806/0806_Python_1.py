from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        now = 0
        for s in S:
            width = widths[ord(s) - 97]
            if now + width > 100:
                line += 1
                now = 0
            now += width
        return [line, now]


if __name__ == "__main__":
    print(Solution().numberOfLines(
        widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        S="abcdefghijklmnopqrstuvwxyz"))  # [3,60]

    print(Solution().numberOfLines(
        widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        S="bbbcccdddaaa"))  # [2,4]
