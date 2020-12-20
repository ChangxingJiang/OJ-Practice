from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        count_row = []
        for row in picture:
            count_row.append(row.count("B"))

        count_col = []
        for col in zip(*picture):
            count_col.append(col.count("B"))

        ans = 0

        for i in range(len(picture)):
            if count_row[i] == 1:
                for j in range(len(picture[i])):
                    if picture[i][j] == "B" and count_col[j] == 1:
                        ans += 1

        return ans


if __name__ == "__main__":
    # 3
    print(Solution().findLonelyPixel([['W', 'W', 'B'],
                                      ['W', 'B', 'W'],
                                      ['B', 'W', 'W']]))
