from typing import List


# 数组 贪心算法
# O(N^2)


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 计算每一行最靠上可以存在的位置
        row_min_idx = []
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    row_min_idx.append(j)
                    break
            else:
                row_min_idx.append(0)

        # print(row_min_idx)

        # 贪心寻找、情景模拟
        ans = 0
        for i in range(n):
            # 如果当前行已符合要求
            if row_min_idx[i] <= i:
                continue

            # 如果当前行不符合要求，寻找符合要求的行
            for j in range(i + 1, n):
                if row_min_idx[j] <= i:
                    ans += j - i
                    row_min_idx = row_min_idx[:i] + [row_min_idx[j]] + row_min_idx[i:j] + row_min_idx[j + 1:]
                    break
            else:
                return -1

        return ans


if __name__ == "__main__":
    print(Solution().minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))  # 3
    print(Solution().minSwaps(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))  # -1
    print(Solution().minSwaps(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]))  # 0
    print(Solution().minSwaps(grid=[[0, 0], [0, 1]]))  # 0
