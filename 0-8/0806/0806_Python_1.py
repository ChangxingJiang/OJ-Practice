from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().numberOfLines(
        widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        S="abcdefghijklmnopqrstuvwxyz"))  # [3,60]

    print(Solution().numberOfLines(
        widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        S="bbbcccdddaaa"))  # [2,4]
