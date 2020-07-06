from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        r = {}
        c = {}
        for index in indices:
            if index[0] not in r:
                r[index[0]] = 1
            else:
                r[index[0]] += 1

            if index[1] not in c:
                c[index[1]] = 1
            else:
                c[index[1]] += 1

        r_odd = 0
        for k in r.values():
            if k % 2 == 1:
                r_odd += 1
        r_even = n - r_odd

        c_odd = 0
        for k in c.values():
            if k % 2 == 1:
                c_odd += 1
        c_even = m - c_odd

        return r_odd * c_even + c_odd * r_even


if __name__ == "__main__":
    print(Solution().oddCells(n=2, m=3, indices=[[0, 1], [1, 1]]))  # 6
    print(Solution().oddCells(n=2, m=2, indices=[[1, 1], [0, 0]]))  # 0
