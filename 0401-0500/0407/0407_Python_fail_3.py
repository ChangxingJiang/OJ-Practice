import collections
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 判断位置是否有效
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        s1, s2 = len(heightMap), len(heightMap[0])

        # 处理池子过小的情况
        # O(1)
        if s1 <= 2 or s2 <= 2:
            return 0

        # 记录每个位置的最大灌水高度
        height = [[-1] * s2 for _ in range(s1)]

        # 从外向内压缩墙的位置，最后圈出的就是池子
        queue = collections.deque()

        # 初始化最外层墙的位置
        # O(M+N)
        for i1 in range(0, s1):
            queue.append((i1, 0))
            queue.append((i1, s2 - 1))
        for i2 in range(0, s2):
            queue.append((0, i2))
            queue.append((s1 - 1, i2))

        # 遍历外墙初步压缩墙
        # O(M×N)
        while queue:
            # 取出当前正在被遍历的位置
            i1, i2 = queue.popleft()
            height[i1][i2] = heightMap[i1][i2]

            # 计算相邻的位置
            neighbours = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 + 1), (i1, i2 - 1)]

            # 检查当前位置四周的位置
            for ii1, ii2 in neighbours:
                if is_valid(ii1, ii2) and height[ii1][ii2] == -1 and heightMap[ii1][ii2] > height[i1][i2]:
                    queue.append((ii1, ii2))

        for row in height:
            print(row)

        # 遍历所有水坑计算容积
        # O(N×M)
        ans = 0
        visited = set()
        for i1 in range(1, s1 - 1):
            for i2 in range(1, s2 - 1):
                # 如果当前位置不是水坑
                if height[i1][i2] != -1 or (i1, i2) in visited:
                    continue

                # 遍历完整的水坑
                min_height = 20001  # 已知高程池壁的最小值
                pool_height = []  # 水坑中的高程列表
                pool_visited = {(i1, i2)}  # 水坑中已经被遍历的位置
                queue = collections.deque([(i1, i2)])  # 水坑中尚未被遍历的位置
                while queue:
                    # 取出当前正在被遍历的位置
                    ii1, ii2 = queue.popleft()
                    pool_height.append(heightMap[ii1][ii2])
                    print(ii1, ii2, "->", heightMap[ii1][ii2])

                    # 计算相邻的位置
                    neighbours = [(ii1 + 1, ii2), (ii1 - 1, ii2), (ii1, ii2 + 1), (ii1, ii2 - 1)]

                    # 检查当前位置四周的位置
                    for iii1, iii2 in neighbours:
                        if height[iii1][iii2] != -1:
                            min_height = min(min_height, height[iii1][iii2])
                        elif (iii1, iii2) not in pool_visited:
                            pool_visited.add((iii1, iii2))
                            queue.append((iii1, iii2))

                print("池壁高度:", min_height)

                # 计算当前水坑总容积
                for now_height in pool_height:
                    ans += min_height - now_height if min_height > now_height else 0

                visited |= pool_visited

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
    print(Solution().trapRainWater([[5, 5, 5, 1],
                                    [5, 1, 1, 5],
                                    [5, 1, 5, 5],
                                    [5, 2, 5, 8]]))

    # 3
    print(Solution().trapRainWater([[10, 10, 10, 10, 10, 10, 10],
                                    [10, 8, 9, 6, 7, 4, 5],
                                    [10, 10, 10, 10, 10, 10, 10]]))
