from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        size = len(colsum)

        count2 = colsum.count(2)
        count1 = colsum.count(1)
        upper -= count2
        lower -= count2
        if upper + lower != count1 or upper < 0 or lower < 0:
            return []

        ans = [[0] * size for _ in range(2)]

        for i in range(size):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
            elif colsum[i] == 1:
                if upper:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1

        return ans


if __name__ == "__main__":
    # [[1,1,0],[0,0,1]]
    print(Solution().reconstructMatrix(upper=2, lower=1, colsum=[1, 1, 1]))

    # []
    print(Solution().reconstructMatrix(upper=2, lower=3, colsum=[2, 2, 1, 1]))

    # [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
    print(Solution().reconstructMatrix(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))
