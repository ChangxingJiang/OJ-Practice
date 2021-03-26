from typing import List


class SegmentTree(object):
    def __init__(self, n):
        self.N = n

        # 计算线段树的高度
        self.H = 1
        while (1 << self.H) < n:
            self.H += 1

        # 初始化线段树数组和lazy属性数组（lazy属性对应所有内部节点）
        self.tree = [float("inf")] * (2 * n)
        self.lazy = [float("inf")] * n

    def _apply(self, x, val):
        """计算x的值，并将x的子节点的计算填写到lazy属性中"""
        self.tree[x] = min(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = min(self.lazy[x], val)  # 每个节点的lazy属性都是给子节点用的

    def _pull(self, x):
        """计算叶节点x及其祖先节点的值"""
        while x > 1:
            x >>= 1
            self.tree[x] = min(self.tree[x * 2], self.tree[x * 2 + 1])
            self.tree[x] = min(self.tree[x], self.lazy[x])

    def _push(self, x):
        """从根节点向下计算x的祖先节点的lazy属性中的值"""
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, h):
        # 计算L和R对应的叶节点坐标
        l += self.N
        r += self.N

        # 从叶节点开始向上更新值
        L0, R0 = l, r
        while l <= r:
            # print("更新区域:", l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                self._apply(l, h)
                l += 1
            if r & 1 == 0:
                self._apply(r, h)
                r -= 1
            # print("当前更新:", self.tree, self.lazy)
            l >>= 1
            r >>= 1

        # 计算叶节点x及其祖先节点的值
        self._pull(L0)
        self._pull(R0)

        # print("更新完成", self.tree, self.lazy)

    def query(self, l, r):
        """查询从L到R（开闭区间）的值"""

        # 计算L和R对应的叶节点坐标
        l += self.N
        r += self.N

        # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
        self._push(l)
        self._push(r)

        # 查询指定范围的和
        ans = float("inf")
        while l <= r:
            # print(l, r, "->", l & 1, r & 1)
            if l & 1 == 1:
                ans = min(ans, self.tree[l])
                l += 1
            if r & 1 == 0:
                ans = min(ans, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ans


class Solution:
    def minJump(self, jump: List[int]) -> int:
        size = len(jump)

        # 定义状态矩阵
        dp = SegmentTree(size + 1)
        dp.update(0, 0, 0)

        for i, n in enumerate(jump):
            # 当前的最小步数
            now = dp.query(i, i)

            # 更新弹簧终点位置的最小步数
            dp.update(min(i + n, size), min(i + n, size), now + 1)

            # 更新弹簧中点位置之前的最小步数
            dp.update(i + 1, min(i + n, size), now + 2)

        return dp.query(size, size)


if __name__ == "__main__":
    print(Solution().minJump(jump=[2, 5, 1, 1, 1, 1]))  # 3
    print(Solution().minJump(jump=[3, 7, 6, 1, 4, 3, 7, 8, 1, 2, 8, 5, 9, 8, 3, 2, 7, 5, 1, 1]))  # 6
