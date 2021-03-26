import collections
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        info = collections.defaultdict(list)
        for i, j in reservedSeats:
            info[i].append(j)

        ans = (10 // 4) * (n - len(info))  # 计算空行数量

        for i in info:
            choice1 = {2, 3, 4, 5}
            choice2 = {4, 5, 6, 7}
            choice3 = {6, 7, 8, 9}
            b1, b2, b3 = True, True, True
            for j in info[i]:
                if j in choice1:
                    b1 = False
                if j in choice2:
                    b2 = False
                if j in choice3:
                    b3 = False
            if b1 and b3:
                ans += 2
            elif b1 or b2 or b3:
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))  # 2
    print(Solution().maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))  # 4

    # 4
    print(Solution().maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))

    # 2
    print(Solution().maxNumberOfFamilies(n=5,
                                         reservedSeats=[[4, 7], [4, 1], [3, 1], [5, 9], [4, 4], [3, 7], [1, 3], [5, 5],
                                                        [1, 6], [1, 8], [3, 9], [2, 9], [1, 4], [1, 9], [1, 10]]))
