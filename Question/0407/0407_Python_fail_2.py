import collections
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        s1, s2 = len(heightMap), len(heightMap[0])

        # 处理池子过小的情况
        # O(1)
        if s1 <= 2 or s2 <= 2:
            return 0

        # 记录每个位置的最大灌水高度
        height = [[-1] * s2 for _ in range(s1)]

        # 将边缘位置设置该位置的高程
        # O(N)
        for i1 in range(0, s1):
            height[i1][0] = heightMap[i1][0]
            height[i1][s2 - 1] = heightMap[i1][s2 - 1]
        for i2 in range(0, s2):
            height[0][i2] = heightMap[0][i2]
            height[s1 - 1][i2] = heightMap[s1 - 1][i2]

        # 逐个遍历每个位置，每发现一个没有遍历的位置，就从该位置开始向四周遍历整个水坑
        # 从上到下，逐行排除该行中所有的水坑
        # 每个位置最多被遍历4次
        # O(N×M)
        for i1 in range(1, s1 - 1):
            for i2 in range(1, s2 - 1):
                # 如果当前位置已被遍历，则跳过当前位置
                if height[i1][i2] != -1:
                    continue
                # 计算当前点的高程
                now_height = heightMap[i1][i2]
                # 如果当前位置的高程高于四周已经遍历的位置，则当前位置不可能存更多的水，即当前位置就是新的池壁
                if (now_height > height[i1 - 1][i2] > -1
                        or now_height > height[i1][i2 - 1] > -1
                        or now_height > height[i1 + 1][i2] > -1
                        or now_height > height[i1][i2 + 1] > -1):
                    height[i1][i2] = now_height
                # 开始遍历完整的水坑
                min_height = 20001  # 已知高程池壁的最小值
                pool = []
                visited = set()  # 水坑中已经被遍历的位置
                queue = collections.deque([(i1, i2)])  # 水坑中尚未被遍历的位置
                while queue:
                    # 取出当前正在被遍历的位置
                    ii1, ii2 = queue.popleft()

                    # 计算相邻的位置
                    neighbours = [(ii1 + 1, ii2), (ii1 - 1, ii2), (ii1, ii2 + 1), (ii1, ii2 - 1)]

                    # 检查当前位置四周的位置
                    for iii1, iii2 in neighbours:
                        if height[iii1][iii2] > -1:
                            min_height = min(min_height, height[iii1][iii2])
                        elif heightMap[iii1][iii2] > min_height:
                            height[iii1][iii2] = heightMap[iii1][iii2]
                        elif (iii1, iii2) not in visited:
                            visited.add((iii1, iii2))
                            queue.append((iii1, iii2))

                print(visited)

                # height[i1][i2] = min(height[i1 - 1][i2], height[i1][i2 - 1])

        for row in height:
            print(row)

        # 计算最终结果
        # O(N×M)
        ans = 0
        for i1 in range(s1):
            for i2 in range(s2):
                if height[i1][i2] > 0 and height[i1][i2] > heightMap[i1][i2]:
                    # print(i1, i2, ":", height[i1][i2], heightMap[i1][i2], "->", height[i1][i2] - heightMap[i1][i2])
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

    # 3
    print(Solution().trapRainWater([[10, 10, 10, 10, 10, 10, 10],
                                    [10, 8, 9, 6, 7, 4, 5],
                                    [10, 10, 10, 10, 10, 10, 10]]))
