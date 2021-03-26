import collections
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        dic_row = collections.defaultdict(list)
        count_row = []
        for i in range(len(picture)):
            row = picture[i]
            count_row.append(row.count("B"))
            if count_row[-1] == N:
                dic_row[tuple(row)].append(i)

        rows = list(dic_row.values())
        row_dic = {}
        for r, lst in enumerate(rows):
            for i in lst:
                row_dic[i] = r

        # print(count_row)
        # print(row_dic)

        ans = 0

        for j in range(len(picture[0])):
            count = 0
            row_lst = []
            for i in range(len(picture)):
                if picture[i][j] == "B":
                    count += 1
                    row_lst.append(i)
            if count == N:
                row_set = set()
                fail = False
                for r in row_lst:
                    if r not in row_dic:
                        fail = True
                        break
                    row_set.add(row_dic[r])
                if not fail and len(row_set) == 1:
                    ans += count

        return ans


if __name__ == "__main__":
    # 6
    print(Solution().findBlackPixel([
        ['W', 'B', 'W', 'B', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'B', 'W'],
        ['W', 'W', 'B', 'W', 'B', 'W']
    ], 3))

    # 0
    print(Solution().findBlackPixel([
        ["W", "B", "W", "B", "B", "W"],
        ["W", "B", "W", "B", "B", "W"],
        ["W", "B", "W", "B", "B", "W"],
        ["B", "W", "B", "W", "W", "B"]
    ], 1))
