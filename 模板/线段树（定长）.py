from typing import Callable, List, Optional


class SegmentTree:
    """定长线段树"""

    def __init__(self, n: int,
                 update_fn_1: Callable[[int, int], int],
                 update_fn_2: Callable[[int, int, int], int],
                 query_fn: Callable[[int, int], int],
                 default_list: Optional[List[int]] = None):
        """线段树的构造方法

        Parameters
        ----------
        n : int
            线段树的长度
        update_fn_1 : Callable[[int, int], int]
            线段树的更新函数 1：根据当前值和需要更新的值，计算更新后的值
        update_fn_2 : Callable[[int, int, int], int]
            线段树的更新函数 2：根据当前值、更新值和下属节点数，计算更新后的值
        query_fn : Callable[[int, int], int]
            线段树的查询函数：根据左右子树的值，计算当前节点的值
        default_list : Optional[List[int]], default = None
            线段树的初始值列表，如果没有提供初始化值列表，则初始化为 0
        """
        self.n = n
        self.update_fn_1 = update_fn_1  # 线段树的更新函数 1
        self.update_fn_2 = update_fn_2  # 线段树的更新函数 2
        self.query_fn = query_fn  # 查询线段树的函数

        if default_list is None:
            default_list = [0] * self.n

        # 简单根据 4 * n 构造数组
        self.tree = [0] * (4 * n)  # 节点值
        self.lazy = [0] * (4 * n)  # 懒惰标记
        self.init_list = default_list

        # 递归初始化线段树（根节点是 1 而不是 0）
        self.build(0, n - 1, 1)

    def build(self, s: int, t: int, p: int):
        """对 [s,t] 区间建立线段树，当前根的编号为 p"""
        if s == t:
            self.tree[p] = self.init_list[s]
            return
        m = s + ((t - s) >> 1)
        # 移位运算符的优先级小于加减法，所以加上括号
        # 如果写成 (s + t) >> 1 可能会超出 int 范围

        self.build(s, m, p * 2)
        self.build(m + 1, t, p * 2 + 1)

        # 递归对左右区间建树
        self.tree[p] = self.query_fn(self.tree[p * 2], self.tree[(p * 2) + 1])

    def update(self, l, r, c):
        """[l, r] 为修改区间，c 为被修改的元素的变化量"""
        self._update(l, r, c, 0, self.n - 1, 1)

    def _update(self, l, r, c, s, t, p):
        # [l, r] 为修改区间, c 为被修改的元素的变化量, [s, t] 为当前节点包含的区间, p 为当前节点的编号

        # 如果当前节点包含的区间 [s, t] 是修改区间 [l, r] 的子集，则仅修改当前节点值和懒惰标记，结束修改
        if l <= s and t <= r:
            self.tree[p] = self.update_fn_2(self.tree[p], c, (t - s + 1))
            self.lazy[p] = self.update_fn_1(self.lazy[p], c)
            return

        # 如果当前节点的懒惰标记不为空，则更新当前节点的两个子节点的值和懒惰标记，并清空当前节点的懒惰标记
        m = s + ((t - s) >> 1)
        if self.lazy[p] and s != t:
            # 更新两个子节点的值
            self.tree[p * 2] = self.update_fn_2(self.tree[p * 2], self.lazy[p], (m - s + 1))
            self.tree[p * 2 + 1] = self.update_fn_2(self.tree[p * 2 + 1], self.lazy[p], (t - m))

            # 更新两个子节点的懒惰标记
            self.lazy[p * 2] = self.update_fn_1(self.lazy[p * 2], self.lazy[p])
            self.lazy[p * 2 + 1] = self.update_fn_1(self.lazy[p * 2 + 1], self.lazy[p])

            # 清空当前节点的懒惰标记
            self.lazy[p] = 0

        # 如果修改区间 [l, r] 与当前节点左子节点包含的区间 [s, m] 存在交集，则递归地更新左子节点
        if l <= m:
            self._update(l, r, c, s, m, p * 2)

        # 如果修改区间 [l, r] 与当前节点右子节点包含的区间 [m + 1, t] 存在交集，则递归地更新右子节点
        if r > m:
            self._update(l, r, c, m + 1, t, p * 2 + 1)

        # 根据左子节点和右子节点的值，更新当前节点的值
        self.tree[p] = self.query_fn(self.tree[p * 2], self.tree[p * 2 + 1])

    def query(self, l, r):
        return self._query(l, r, 0, self.n - 1, 1)

    def _query(self, l, r, s, t, p):
        # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p为当前节点的编号

        # 如果当前节点包含的区间 [s, t] 是查询区间 [l, r] 的子集，则直接返回当前节点值
        if l <= s and t <= r:
            return self.tree[p]

        # 如果当前节点的懒惰标记不为空，则更新当前节点的两个子节点的值和懒惰标记，并清空当前节点的懒惰标记
        m = s + ((t - s) >> 1)
        if self.lazy[p]:
            # 更新两个子节点的值
            self.tree[p * 2] = self.update_fn_2(self.tree[p * 2], self.lazy[p], (m - s + 1))
            self.tree[p * 2 + 1] = self.update_fn_2(self.tree[p * 2 + 1], self.lazy[p], (t - m))

            # 更新两个子节点的懒惰标记
            self.lazy[p * 2] = self.update_fn_1(self.lazy[p * 2], self.lazy[p])
            self.lazy[p * 2 + 1] = self.update_fn_1(self.lazy[p * 2 + 1], self.lazy[p])

            # 清空当前节点的懒惰标记
            self.lazy[p] = 0

        # 如果查询区间 [l, r] 与当前节点左子节点包含的区间 [s, m] 存在交集，且与当前节点右子节点包含的区间 [m + 1, t] 存在交集
        if l <= m and r > m:
            return self.query_fn(self._query(l, r, s, m, p * 2), self._query(l, r, m + 1, t, p * 2 + 1))

        # 如果查询区间 [l, r] 仅与当前节点左子节点包含的区间 [s, m] 存在交集
        if l <= m:
            return self._query(l, r, s, m, p * 2)

        # 如果查询区间 [l, r] 与当前节点右子节点包含的区间 [m + 1, t] 存在交集
        if r > m:
            return self._query(l, r, m + 1, t, p * 2 + 1)

        # 应该不会到达这个位置
        return 0


if __name__ == "__main__":
    # 样例：批量加法更新，计算最大值
    sg = SegmentTree(4,
                     update_fn_1=lambda x, y: x + y,
                     update_fn_2=lambda x, y, z: x + y,
                     query_fn=max,
                     default_list=[0, 1, 2, 3])
