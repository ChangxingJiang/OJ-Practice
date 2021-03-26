from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), max(len(row) for row in nums)

        table = [[] for _ in range(n + m - 1)]
        for i in range(m):
            for j in range(len(nums[i])):
                table[i + j].append(nums[i][j])

        ans = []
        for row in table:
            ans.extend(reversed(row))
        return ans


if __name__ == "__main__":
    # [1,4,2,7,5,3,8,6,9]
    print(Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
    print(Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))

    # [1,4,2,5,3,8,6,9,7,10,11]
    print(Solution().findDiagonalOrder(nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))

    # [1,2,3,4,5,6]
    print(Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5, 6]]))
