import collections
from typing import List


class Solution:
    class Node:
        def __init__(self, points, children=None, father=None):
            if children is None:
                children = set()
            if father is None:
                father = set()

            self.points = points  # 兄弟节点列表
            self.children = children  # 子节点列表
            self.father = father  # 父节点列表

        def merge(self, other):
            self.points += other.points
            self.children += other.children
            self.father += other.father

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        s1, s2 = len(matrix), len(matrix[0])

        # 构造节点对象列表
        nodes = [[self.Node([(i1, i2)]) for i2 in range(s2)] for i1 in range(s1)]

        # 构造行中各个节点之间的关系（从小指向大）
        for i1 in range(s1):
            count = collections.defaultdict(list)
            for i2 in range(s2):
                count[matrix[i1][i2]].append(i2)

            sorted_val = list(sorted(count.keys()))
            last = []
            for val in sorted_val:
                # 合并兄弟节点
                now = count[val]
                ii2 = now[0]
                for i2 in range(1, len(now)):
                    nodes[i1][i2].merge(nodes[i1][ii2])
                    nodes[i1][ii2] = nodes[i1][ii2]

            # 排序当前行中各个节点
            lst = [(matrix[i1][j], j) for j in range(s2)]
            lst.sort()

            # 合并兄弟节点
            piece = []
            for j in range(s2):
                if j == 0 or lst[j][0] != lst[j - 1][0]:
                    piece.append([lst[j][1]])
                else:
                    piece[-1].append(lst[j][1])

            # 生成节点之间的关系
            last = piece[0]
            for jj in range(1, len(piece)):
                now = piece[jj]
                for j1 in last:
                    for j2 in now:
                        nodes[i1][j1].children.add(nodes[i1][j2])
                        count[(i1, j2)] += 1
                last = now

        # 构造列中各个节点之间的关系（从小指向大）
        for j in range(s2):
            # 排序当前列中各个节点
            lst = [(matrix[i][j], i) for i in range(s1)]
            lst.sort()

            # 生成当前列表中的每一段相同值
            piece = []
            for i in range(s1):
                if i == 0 or lst[i][0] != lst[i - 1][0]:
                    piece.append([lst[i][1]])
                else:
                    piece[-1].append(lst[i][1])

            # 生成节点之间的关系
            last = piece[0]
            for ii in range(1, len(piece)):
                now = piece[ii]
                for i1 in last:
                    for i2 in now:
                        nodes[i1][j].children.add(nodes[i2][j])
                        count[(i2, j)] += 1
                last = now

        # ----------拓扑排序----------
        ans = [[0] * s2 for _ in range(s1)]

        # 寻找没有父节点的节点
        queue = collections.deque()
        for point, num in count.items():
            if num == 0:
                queue.append(point)

        step = 1
        while queue:
            # print(step, ":", count)
            for _ in range(len(queue)):
                (i, j) = queue.popleft()
                ans[i][j] = step
                for node in nodes[i][j].children:
                    count[(node.i, node.j)] -= 1
                    if count[(node.i, node.j)] == 0:
                        queue.append((node.i, node.j))
            step += 1

        # print(ans)
        # print(dsu.array)

        # ----------并查集合并应相同的秩----------
        # 将并查集的根节点更新为最终结果
        for i1 in range(s1):
            for j1 in range(s2):
                idx1 = i1 * s2 + j1
                idx2 = dsu.find(idx1)
                i2, j2 = divmod(idx2, s2)
                # print((i1, j1), ":", idx1, "->", (i2, j2), ":", idx2)
                ans[i2][j2] = max(ans[i2][j2], ans[i1][j1])

        # 将并查集的非根节点更新为根节点的值
        for i1 in range(s1):
            for j1 in range(s2):
                idx1 = i1 * s2 + j1
                idx2 = dsu.find(idx1)
                i2, j2 = divmod(idx2, s2)
                ans[i1][j1] = ans[i2][j2]

        return ans


if __name__ == "__main__":
    # [[1,2],
    #  [2,3]]
    print(Solution().matrixRankTransform(matrix=[
        [1, 2],
        [3, 4]
    ]))

    # [[1,1],
    #  [1,1]]
    print(Solution().matrixRankTransform(matrix=[
        [7, 7],
        [7, 7]
    ]))

    # [[4,2,3],
    #  [1,3,4],
    #  [5,1,6],
    #  [1,3,4]]
    print(Solution().matrixRankTransform(matrix=[
        [20, -21, 14],
        [-19, 4, 19],
        [22, -47, 24],
        [-19, 4, 19]
    ]))

    # [[5,1,4],
    #  [1,2,3],
    #  [6,3,1]]
    print(Solution().matrixRankTransform(matrix=[
        [7, 3, 6],
        [1, 4, 5],
        [9, 8, 2]
    ]))

    # [[2,1,4,6],
    #  [2,6,5,4],
    #  [5,2,4,3],
    #  [4,3,1,5]]
    print(Solution().matrixRankTransform(matrix=[
        [-37, -50, -3, 44],
        [-37, 46, 13, -32],
        [47, -42, -3, -40],
        [-17, -22, -39, 24]
    ]))

    # [[7,13,1,5,4,6,9,8],
    #  [8,11,2,10,1,12,14,9],
    #  [2,14,1,11,13,7,5,3],
    #  [3,19,16,12,14,7,10,13],
    #  [8,12,6,14,5,1,4,13],
    #  [2,16,15,17,4,18,3,14],
    #  [3,7,11,6,12,13,14,10],
    #  [16,19,18,3,15,2,11,17]]
    print(Solution().matrixRankTransform(matrix=[
        [-23, 20, -49, -30, -39, -28, -5, -14],
        [-19, 4, -33, 2, -47, 28, 43, -6],
        [-47, 36, -49, 6, 17, -8, -21, -30],
        [-27, 44, 27, 10, 21, -8, 3, 14],
        [-19, 12, -25, 34, -27, -48, -37, 14],
        [-47, 40, 23, 46, -39, 48, -41, 18],
        [-27, -4, 7, -10, 9, 36, 43, 2],
        [37, 44, 43, -38, 29, -44, 19, 38]
    ]))
