import collections
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        s1, s2 = len(heightMap), len(heightMap[0])
        if not s1 or not s2:
            return 0

        # 分别计算上下左右的高度
        # O(4×N×M)
        height1, height2, height3, height4 = [], [], [[] for _ in range(s1)], [[] for _ in range(s1)]
        for i1 in range(s1):
            height1.append([])
            last = 0
            for i2 in range(s2):
                height1[-1].append(last)
                last = max(last, heightMap[i1][i2])
        for i1 in range(s1):
            height2.append([])
            last = 0
            for i2 in range(s2 - 1, -1, -1):
                height2[-1].append(last)
                last = max(last, heightMap[i1][i2])
            height2[-1].reverse()
        for i2 in range(s2):
            last = 0
            for i1 in range(s1):
                height3[i1].append(last)
                last = max(last, heightMap[i1][i2])
        for i2 in range(s2):
            last = 0
            for i1 in range(s1 - 1, -1, -1):
                height4[i1].append(last)
                last = max(last, heightMap[i1][i2])

        # 计算临时储水高度
        # O(N×M)
        height = [[0] * s2 for _ in range(s1)]
        for i1 in range(s1):
            for i2 in range(s2):
                h = min(height1[i1][i2], height2[i1][i2], height3[i1][i2], height4[i1][i2])
                if h > heightMap[i1][i2]:
                    height[i1][i2] = h

        # 统一每个水池的最大高度
        # O(N×M)
        visited = set()
        for i1 in range(s1):
            for i2 in range(s2):
                if height[i1][i2] > 0 and (i1, i2) not in visited:
                    # 寻找当前水池的所有位置
                    now = {(i1, i2)}
                    wait = collections.deque([(i1, i2)])
                    min_height = height[i1][i2]  # 当前水池最低高度
                    while wait:
                        ii1, ii2 = wait.popleft()
                        if ii1 < s1 and height[ii1 + 1][ii2] and (ii1 + 1, ii2) not in now:
                            min_height = min(min_height, height[ii1 + 1][ii2])
                            now.add((ii1 + 1, ii2))
                            wait.append((ii1 + 1, ii2))
                        if ii1 > 0 and height[ii1 - 1][ii2] and (ii1 - 1, ii2) not in now:
                            min_height = min(min_height, height[ii1 - 1][ii2])
                            now.add((ii1 - 1, ii2))
                            wait.append((ii1 - 1, ii2))
                        if ii2 < s2 and height[ii1][ii2 + 1] and (ii1, ii2 + 1) not in now:
                            min_height = min(min_height, height[ii1][ii2 + 1])
                            now.add((ii1, ii2 + 1))
                            wait.append((ii1, ii2 + 1))
                        if ii2 > 0 and height[ii1][ii2 - 1] and (ii1, ii2 - 1) not in now:
                            min_height = min(min_height, height[ii1][ii2 - 1])
                            now.add((ii1, ii2 - 1))
                            wait.append((ii1, ii2 - 1))

                    # 将当前水池所有位置同步为最低高度
                    for ii1, ii2 in now:
                        height[ii1][ii2] = min_height

                    visited |= now

        for row in height:
            print(row)

        # 计算最终结果
        # O(N×M)
        ans = 0
        for i1 in range(s1):
            for i2 in range(s2):
                if height[i1][i2] > 0 and height[i1][i2] > heightMap[i1][i2]:
                    print(i1, i2, ":", height[i1][i2], heightMap[i1][i2], "->", height[i1][i2] - heightMap[i1][i2])
                    ans += height[i1][i2] - heightMap[i1][i2]

        return ans


if __name__ == "__main__":
    # 4
    print(Solution().trapRainWater([[1, 4, 3, 1, 3, 2],
                                    [3, 2, 1, 3, 2, 4],
                                    [2, 3, 3, 2, 3, 1]]))

    # 14
    print(Solution().trapRainWater([[12, 13, 1, 12],
                                    [13, 4, 13, 12],
                                    [13, 8, 10, 12],
                                    [12, 13, 12, 12],
                                    [13, 13, 13, 13]]))

    # 44
    print(Solution().trapRainWater([[78, 16, 94, 36],
                                    [87, 93, 50, 22],
                                    [63, 28, 91, 60],
                                    [64, 27, 41, 27],
                                    [73, 37, 12, 69],
                                    [68, 30, 83, 31],
                                    [63, 24, 68, 36]]))
