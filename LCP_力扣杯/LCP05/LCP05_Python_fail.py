from typing import List


class SegmentTreeForSum(object):
    """求和线段树"""

    def __init__(self, n, default=0):
        self.n = n
        self.default = default

        # 计算线段树的内部节点数量
        self.M = (self.n - 1) // 2 * 2 + 1

        # 计算线段树的高度
        self.H = 1
        while (1 << self.H) < (self.M + self.n):
            self.H += 1

        # 初始化数组表示的线段树（长度为内部节点数+叶子节点数）
        # 如果最后一个节点是其父节点的左节点的话，则为其多补出一个右节点，以避免超出
        self.tree = [self.default] * ((self.M + self.n) if (self.M + self.n) % 2 == 1 else (self.M + self.n + 1))

        # 初始化内部节点的lazy属性数组（长度为内部节点数）
        self.lazy = [self.default] * self.M

        # print("线段树的高度:", self.H, "线段树的内部节点数:", self.M)

    def _apply(self, x, val, lazy):
        """更新x节点的值

        更新包括x节点自身的值和当前节点的子节点的值，其中子节点的值通过更新当前节点的lazy属性实现

        :param x: 当前节点在数组中的坐标
        :param val: 当前节点需要更新的目标值
        """
        self.tree[x] += val
        if x < self.M:  # 如果当前节点不是叶节点则更新当前节点的lazy属性
            self.lazy[x] += lazy

    def _pull(self, x):
        """更新节点x的父节点到根节点的值

        :param x: x节点在数组中的坐标
        """
        while x >= 1:
            x = (x - 1) // 2
            print("[线段树:PULL]", x, "<-", (x * 2 + 1, x * 2 + 2), "=", self.tree[x * 2 + 1], "+", self.tree[x * 2 + 2])

            # 计算当前节点仅受子节点影响的值
            self.tree[x] = self.tree[x * 2 + 1] + self.tree[x * 2 + 2]

    def _push(self, x):
        """计算节点x到根节点之间的所有节点的lazy属性，将lazy属性中的值计算到节点值中，并将lazy属性清空

        :param x: x节点在数组中的坐标
        """
        for h in range(self.H, 0, -1):
            y = (x - 1) >> h
            # print("[线段树:PUSH]", x, "->", y, "->", (y * 2 + 1, y * 2 + 2))
            if self.lazy[y]:
                self._apply(y * 2 + 1, self.lazy[y], self.lazy[y])
                self._apply(y * 2 + 2, self.lazy[y], self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, h):
        """更新从l到r之间（闭闭区间）的值

        更新流程：
        1. 计算l和r对应叶子节点在数组中的坐标

        """
        # 计算l和r对应叶子节点在数组中的坐标
        l += self.M
        r += self.M

        lazy = h

        # 从叶节点开始向上更新值
        l0, r0 = l, r
        while 0 < l <= r:
            print("[线段树:UPDATE]", l, "(" + str(l & 1 == 0) + ")", r, "(" + str(r & 1 == 1) + ")", "->", h)

            # 左侧边缘为右节点，则记录左侧边缘进入右侧树
            if l % 2 == 0:
                self._apply(l, h, lazy)
                l += 1

            # 右侧边缘为左节点，则记录右侧边缘进入左侧树
            if r % 2 == 1:
                self._apply(r, h, lazy)
                r -= 1
            l = (l - 1) // 2
            r = (r - 1) // 2
            h *= 2

        # 计算叶节点x及其祖先节点的值
        l, r = l0, r0
        while 0 < l < r and l % 2 == 1:
            l = (l - 1) // 2

            if r % 2 == 1:
                r -= 1
            r = (r - 1) // 2
        self._pull(l)

        while 0 < l < r and l % 2 == 0:
            if l % 2 == 0:
                l += 1
            l = (l - 1) // 2

            r = (r - 1) // 2
        self._pull(r)

    def query(self, l, r):
        """查询从L到R（闭闭区间）的值"""

        # 计算L和R对应的叶节点坐标
        l += self.M
        r += self.M

        # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
        self._push(l)
        self._push(r)

        # 查询指定范围的和
        ans = self.default
        while 0 < l <= r:
            # print("[线段树:QUERY]", l, "(" + str(l & 1 == 0) + ")", r, "(" + str(r & 1 == 1) + ")",
            #       "=", ans, "->", end=" ")

            # 左侧边缘为右节点，则记录左侧边缘进入右侧树
            if l % 2 == 0:
                ans += self.tree[l]
                l += 1

            # 右侧边缘为左节点，则记录右侧边缘进入左侧树
            if r % 2 == 1:
                ans += self.tree[r]
                r -= 1
            # print(ans)
            l = (l - 1) // 2
            r = (r - 1) // 2
        return ans


class Solution:
    class _OriginalNode:
        __slots__ = ("idx", "n", "val", "father", "children")

        def __init__(self, idx):
            self.idx = idx
            self.n = 1  # 树包含的节点数（包含自身）
            self.val = 0  # 树自身的值
            self.father = 0  # 树的父节点
            self.children = set()  # 树的子节点列表

    class _Node:
        __slots__ = ("start", "end")

        def __init__(self):
            self.start = 0  # 树的开始位置
            self.end = 0  # 树的结束位置

    def __init__(self):
        self.dict = {}  # 原始节点坐标和前序序列坐标对应表
        self.original_tree = []  # 原始结构树
        self.tree = []  # 前序序列结构树

    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        # ---------- 将树转换为前序序列 ----------
        # 构造树节点
        # O(N)
        self.original_tree = [self._OriginalNode(i) for i in range(n + 1)]

        # 构造线段树的领导关系
        # O(N)
        for a, b in leadership:
            self.original_tree[a].children.add(b)
            self.original_tree[b].father = a

        # 计算树中每个节点包含的节点数量
        # O(N)
        self.dfs1(1)

        # 构造树的前序序列结构节点
        # O(N)
        self.tree = [self._Node() for _ in range(n + 1)]

        # 构造树的前序序列结构
        # O(N)
        self.dfs2(1, start=0)

        # ---------- 构造线段树 ----------
        def _sum(x, y):
            return x + y

        T = SegmentTreeForSum(n)

        # ---------- 执行操作 ----------

        ans = []

        for operation in operations:
            # 第1种操作：给团队的一个成员（也可以是负责人）发一定数量的LeetCoin
            if operation[0] == 1:
                idx = self.dict[operation[1]]
                value = operation[2]
                T.update(idx, idx, value)
                print("更新区间:", (idx, idx), "=", value)

            # 第2种操作：给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin
            elif operation[0] == 2:
                idx = self.dict[operation[1]]
                l, r = self.tree[idx].start, self.tree[idx].end
                value = operation[2]
                T.update(l, r, value)
                print("更新区间:", (l, r), "=", value)
                # print([T.query(i, i) for i in range(n)], T.query(0, n - 1))

            # 第3种操作：查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和
            else:
                idx = self.dict[operation[1]]
                l, r = self.tree[idx].start, self.tree[idx].end
                ans.append(T.query(l, r) % 1000000007)
                print("查询区间:", (l, r), "=", T.query(l, r) % 1000000007)

        return ans

    def dfs1(self, now):
        """计算线段树中每个节点包含的子节点数量"""
        self.original_tree[now].n = 1
        for child in self.original_tree[now].children:
            self.original_tree[now].n += self.dfs1(child)
        return self.original_tree[now].n

    def dfs2(self, now, start):
        """构造树的前序序列结构"""
        num = self.original_tree[now].n
        idx = start
        self.tree[idx].start, self.tree[idx].end = start, start + num - 1
        self.dict[now] = idx
        idx += 1  # 当前节点自身位置
        for child in self.original_tree[now].children:
            self.dfs2(child, idx)
            idx += self.original_tree[child].n


if __name__ == "__main__":
    # [650, 665]
    print(Solution().bonus(n=6,
                           leadership=[[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]],
                           operations=[[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
                           ))
