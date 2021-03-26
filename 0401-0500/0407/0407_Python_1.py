import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 判断位置是否有效
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        # 海平面不断升高淹没盆地思路
        s1, s2 = len(heightMap), len(heightMap[0])
        s = s1 * s2

        # 处理池子过小的情况
        # O(1)
        if s1 <= 2 or s2 <= 2:
            return 0

        # 计算最外层堤坝位置
        # O(M+N)
        wall_list = []
        for i1 in range(0, s1):
            wall_list.append((i1, 0))
            wall_list.append((i1, s2 - 1))
        for i2 in range(0, s2):
            wall_list.append((0, i2))
            wall_list.append((s1 - 1, i2))

        # 处理最外层堤坝高度
        visited = set()
        heap = []
        for i1, i2 in wall_list:
            heap.append((heightMap[i1][i2], i1, i2))
            visited.add((i1, i2))

        # 使最外层堤坝高度具有堆的特征
        heapq.heapify(heap)

        # 初始化海平面高度
        now_height = 0

        # 开始提升海平面高度直至只剩下狭长（中间不包括被堤坝包围的陆地）岛屿
        ans = 0
        while len(visited) < s:
            # 从堤坝高度堆中取出最低的堤坝
            height, i1, i2 = heapq.heappop(heap)

            # 升高（或不用升高）海平面至可以淹没堤坝的高度
            now_height = max(now_height, height)

            # 计算堤坝周围的坐标位置
            neighbours = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 + 1), (i1, i2 - 1)]

            # 计算堤坝周围的非堤坝或海洋位置（腹地位置）
            inners = [neighbour for neighbour in neighbours if
                      (is_valid(neighbour[0], neighbour[1]) and neighbour not in visited)]

            # 检查腹地位置的淹没情况
            for ii1, ii2 in inners:
                # 如果腹地位置比当前海平面低，则可以增加积水量
                if heightMap[ii1][ii2] < now_height:
                    ans += now_height - heightMap[ii1][ii2]

                # 将当前腹地位置作为新的堤坝
                heapq.heappush(heap, (heightMap[ii1][ii2], ii1, ii2))
                visited.add((ii1, ii2))

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
