from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)

        def count(di, dj):
            res = 0
            for i2 in range(size):
                for j2 in range(size):
                    if 0 <= i2 + di < size and 0 <= j2 + dj < size and img1[i2 + di][j2 + dj] == img2[i2][j2] == 1:
                        res += 1
            return res

        ans = 0
        for i1 in range(-size + 1, size):
            for j1 in range(-size + 1, size):
                ans = max(ans, count(i1, j1))
        return ans


if __name__ == "__main__":
    # 3
    print(Solution().largestOverlap(img1=[[1, 1, 0],
                                          [0, 1, 0],
                                          [0, 1, 0]],
                                    img2=[[0, 0, 0],
                                          [0, 1, 1],
                                          [0, 0, 1]]))
