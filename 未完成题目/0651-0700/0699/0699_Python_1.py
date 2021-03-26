from typing import List


# class SegmentTree(object):
#     def __init__(self, N, update_fn, query_fn):
#         self.N = N
#         self.update_fn = update_fn
#         self.query_fn = query_fn
#
#         # 计算线段树的高度
#         self.H = 1
#         while (1 << self.H) < N:
#             self.H += 1
#
#         # 初始化线段树数组和lazy属性数组（lazy属性对应所有内部节点）
#         self.tree = [0] * (2 * N)
#         self.lazy = [0] * N
#
#     def _apply(self, x, val):
#         """更新当前节点的值
#
#         更新包括当前节点自身的值和当前节点的子节点的值，其中子节点的值通过更新当前节点的lazy属性实现
#
#         :param x: 当前节点在数组中的坐标
#         :param val: 当前节点需要更新的目标值
#         """
#         self.tree[x] = self.update_fn(self.tree[x], val)
#         if x < self.N:  # 如果当前节点不是叶节点则更新当前节点的lazy属性
#             self.lazy[x] = self.update_fn(self.lazy[x], val)
#
#     def _pull(self, x):
#         """计算叶节点x及其祖先节点的值
#
#         :param x:
#         :return:
#         """
#         while x > 1:
#             x >>= 1
#             print("PULL:", x)
#             self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
#             self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])
#
#     def _push(self, x):
#         """从根节点向下计算x的祖先节点的lazy属性中的值"""
#         for h in range(self.H, 0, -1):
#             y = x >> h
#             if self.lazy[y]:
#                 self._apply(y * 2, self.lazy[y])
#                 self._apply(y * 2 + 1, self.lazy[y])
#                 self.lazy[y] = 0
#
#     def update(self, l, r, h):
#         """更新从l到r之间的值
#
#         更新流程：
#         1. 计算l和r对应叶子节点在数组中的坐标
#
#         """
#         # 计算l和r对应叶子节点在数组中的坐标
#         l += self.N
#         r += self.N
#         print("UPDATE1:", "叶子节点坐标:", l, r)
#
#         # 从叶节点开始向上更新值
#         L0, R0 = l, r
#         while l <= r:
#             print("更新区域:", l, r, "->", l & 1, r & 1)
#             if l & 1 == 1:
#                 print("更新:", L0, "->", l, "=", h)
#                 self._apply(l, h)
#                 l += 1
#             if r & 1 == 0:
#                 print("更新:", R0, "->", r, "=", h)
#                 self._apply(r, h)
#                 r -= 1
#             print("当前更新:", self.tree, self.lazy)
#             l >>= 1
#             r >>= 1
#
#         # 计算叶节点x及其祖先节点的值
#         self._pull(L0)
#         self._pull(R0)
#
#         print("更新完成", self.tree, self.lazy)
#
#     def query(self, l, r):
#         """查询从L到R（开闭区间）的值"""
#
#         # 计算L和R对应的叶节点坐标
#         l += self.N
#         r += self.N
#
#         # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
#         self._push(l)
#         self._push(r)
#
#         # 查询指定范围的和
#         ans = 0
#         while l <= r:
#             # print(l, r, "->", l & 1, r & 1)
#             if l & 1 == 1:
#                 ans = self.query_fn(ans, self.tree[l])
#                 l += 1
#             if r & 1 == 0:
#                 ans = self.query_fn(ans, self.tree[r])
#                 r -= 1
#             l >>= 1
#             r >>= 1
#         return ans


class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.update_fn = update_fn
        self.query_fn = query_fn

        # 计算线段树的内部节点数量
        self.M = (self.N - 1) // 2 * 2 + 1

        # 计算线段树的高度
        self.H = 1
        while (1 << self.H) < (self.M + self.N):
            self.H += 1

        # 初始化数组表示的线段树（长度为内部节点数+叶子节点数）
        self.tree = [0] * (self.M + self.N)

        # 初始化内部节点的lazy属性数组（长度为内部节点数）
        self.lazy = [0] * self.M

        print("线段树的高度:", self.H, "线段树的内部节点数:", self.M)

    def _apply(self, x, val):
        """更新x节点的值

        更新包括x节点自身的值和当前节点的子节点的值，其中子节点的值通过更新当前节点的lazy属性实现

        :param x: 当前节点在数组中的坐标
        :param val: 当前节点需要更新的目标值
        """
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.M:  # 如果当前节点不是叶节点则更新当前节点的lazy属性
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        """更新节点x及其祖先节点的值

        :param x: x节点在数组中的坐标
        """
        while x >= 1:
            x //= 2

            # 计算当前节点仅受子节点影响的值
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])

            # 计算当前节点受lazy属性影响的值
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        """计算节点x到根节点之间的所有节点的lazy属性，将lazy属性中的值计算到节点值中，并将lazy属性清空

        :param x: x节点在数组中的坐标
        """
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, h):
        """更新从l到r之间的值

        更新流程：
        1. 计算l和r对应叶子节点在数组中的坐标

        """
        # 计算l和r对应叶子节点在数组中的坐标
        l += self.M
        r += self.M

        # 从叶节点开始向上更新值
        l0, r0 = l, r
        while l <= r:
            if l & 1 == 1:
                self._apply(l, h)
                l += 1
            if r & 1 == 0:
                self._apply(r, h)
                r -= 1
            l >>= 1
            r >>= 1

        # 计算叶节点x及其祖先节点的值
        self._pull(l0)
        self._pull(r0)

        print("更新完成", self.tree, self.lazy)

    def query(self, l, r):
        """查询从L到R（开闭区间）的值"""

        # 计算L和R对应的叶节点坐标
        l += self.M
        r += self.M

        # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
        self._push(l)
        self._push(r)

        # 查询指定范围的和
        ans = 0
        while l <= r:
            # print(l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                ans = self.query_fn(ans, self.tree[l])
                l += 1
            if r & 1 == 0:
                ans = self.query_fn(ans, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ans


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        size = 0
        for position in positions:
            size = max(size, position[0] + position[1] + 1)

        st = SegmentTree(size, max, max)

        highest = 0
        ans = []
        for left, size in positions:
            h = st.query(left, left + size - 1) + size
            print("Left:", left, "Right:", left + size - 1, "查询结果:", h - size, "更新结果:", h)
            st.update(left, left + size - 1, h)
            highest = max(highest, h)
            ans.append(highest)

        return ans


if __name__ == "__main__":
    # [2,5,5]
    print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))

    # [100, 100]
    print(Solution().fallingSquares([[100, 100], [200, 100]]))
