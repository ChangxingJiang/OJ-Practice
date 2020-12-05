# LeetCode题解(LCP05)：团队成员发硬币(Python)

题目：[原题链接](https://leetcode-cn.com/problems/coin-bonus/)（困难）

标签：线段树

| 解法           | 时间复杂度                                         | 空间复杂度 | 执行用时        |
| -------------- | -------------------------------------------------- | ---------- | --------------- |
| Ans 1 (Python) | 每次操作 = $O(N)$ (在每个节点只有一个子节点时出现) | $O(N)$     | 超出时间限制    |
| Ans 2 (Python) | 每次操作 = $O(logN)$                               | $O(N)$     | 3464ms (49.06%) |
| Ans 3 (Python) |                                                    |            |                 |

解法一（将每个成员作为节点的包含lazy属性的树结构）：

```python
class Solution:
    # 思路：线段树

    class _Node:
        def __init__(self, idx):
            self.idx = idx
            self.n = 1  # 树包含的节点数（包含自身）
            self.val = 0  # 树自身的值
            self.lazy = 0  # 树尚未计算的值
            self.father = 0  # 树的父节点
            self.children = set()  # 树的子节点列表

    def __init__(self):
        self.tree = []

    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        # 构造线段树节点
        self.tree = [self._Node(i) for i in range(n + 1)]

        # 构造线段树的领导关系
        for a, b in leadership:
            self.tree[a].children.add(b)
            self.tree[b].father = a

        # 计算树中每个节点包含的节点数量
        self.dfs(1)

        ans = []

        # 执行操作
        for operation in operations:
            # 第1种操作：给团队的一个成员（也可以是负责人）发一定数量的LeetCoin
            if operation[0] == 1:
                now, value = operation[1], operation[2]
                # 将当前新增值不断向上传递，直到传递到负责人
                while now > 0:
                    self.tree[now].val += value
                    now = self.tree[now].father

            # 第2种操作：给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin
            elif operation[0] == 2:
                # 依据当前成员包含的节点数量，计算增加总量
                now, value = operation[1], self.tree[operation[1]].n * operation[2]
                # 将当前新增值不断向上传递，直到传递到负责人（同样更新了当前节点）
                while now > 0:
                    self.tree[now].val += value
                    now = self.tree[now].father
                # 将当前新值需要向下传递的记录到lazy中
                self.tree[operation[1]].lazy += operation[2]

            # 第3种操作：查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和
            else:
                # 计算所有父节点的列表
                stack = []
                now = operation[1]
                while now > 0:
                    stack.append(now)
                    now = self.tree[now].father
                # 计算所有父节点的lazy属性
                while stack:
                    now = stack.pop()
                    if self.tree[now].lazy > 0:
                        for child in self.tree[now].children:
                            self.tree[child].val += self.tree[child].n * self.tree[now].lazy
                            self.tree[child].lazy += self.tree[now].lazy
                        self.tree[now].lazy = 0
                # print(operation, "->", self.tree[operation[1]].val % 1000000007)
                ans.append(self.tree[operation[1]].val % 1000000007)

        return ans

    def dfs(self, now):
        """计算线段树中每个节点包含的子节点数量"""
        self.tree[now].n = 1
        for child in self.tree[now].children:
            self.tree[now].n += self.dfs(child)
        return self.tree[now].n
```

解法二（转成树的前序序列用包含lazy属性的线段树求解）：

```python
class SegmentTreeForSum(object):
    """求和线段树"""

    class _Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.val = 0
            self.left = None
            self.right = None
            self.lazy = 0

    def _build_tree(self, root):
        """构造线段树"""
        if root.start == root.end:
            return
        else:
            mid = (root.start + root.end) // 2
            root.left = self._Node(root.start, mid)
            root.right = self._Node(mid + 1, root.end)
            self._build_tree(root.left)
            self._build_tree(root.right)

    def __init__(self, n):
        """初始化线段树实例"""
        self.root = self._Node(0, n - 1)
        self._build_tree(self.root)

    def _update_interval(self, root, start, end, data):
        """更新在节点root上更新[start, end]区间的数据"""

        # 处理节点刚好可以表示区间的情况：不再进行分裂，累加lazy值
        if root.start == start and root.end == end:
            root.val += data * (root.end - root.start + 1)
            root.lazy += data
            return root.val

        # 处理节点需要继续分裂的情况
        else:
            mid = (root.start + root.end) // 2

            # 处理当前节点的lazy属性
            if root.lazy > 0:
                root.left.val += (mid - root.start + 1) * root.lazy
                root.left.lazy += root.lazy

                root.right.val += (root.end - (mid + 1) + 1) * root.lazy
                root.right.lazy += root.lazy
                root.lazy = 0

            # 处理分裂的情况
            if end <= mid:
                v = self._update_interval(root.left, start, end, data)
                root.val = v + root.right.val
            elif start >= mid + 1:
                v = self._update_interval(root.right, start, end, data)
                root.val = root.left.val + v
            else:
                v1 = self._update_interval(root.left, start, mid, data)
                v2 = self._update_interval(root.right, mid + 1, end, data)
                root.val = v1 + v2

            return root.val

    # 更新单个数据
    def _update_single(self, root, idx, data):
        # 处理节点已经找到的情况
        if root.start == root.end and root.start == idx:
            root.val += data
            return root.val

        # 处理节点尚未找到的情况：二分寻找当前节点
        else:
            mid = (root.start + root.end) // 2

            # 处理当前节点的lazy属性
            if root.lazy > 0:
                root.left.val += (mid - root.start + 1) * root.lazy
                root.left.lazy += root.lazy

                root.right.val += (root.end - (mid + 1) + 1) * root.lazy
                root.right.lazy += root.lazy
                root.lazy = 0

            # 处理分裂的情况
            if idx <= mid:
                root.val = self._update_single(root.left, idx, data) + root.right.val
            else:
                root.val = root.left.val + self._update_single(root.right, idx, data)

            return root.val

    # 获取区间数据
    def _get_data(self, root, start, end):
        # 处理节点刚好可以表示区间的情况
        if root.start == start and root.end == end:
            return root.val

        # 处理节点需要继续分裂的情况
        else:
            mid = (root.start + root.end) // 2

            # 处理当前节点的lazy属性
            if root.lazy > 0:
                root.left.val += (mid - root.start + 1) * root.lazy
                root.left.lazy += root.lazy

                root.right.val += (root.end - (mid + 1) + 1) * root.lazy
                root.right.lazy += root.lazy
                root.lazy = 0

            # 处理分裂的情况
            if end <= mid:
                return self._get_data(root.left, start, end)
            elif start >= mid + 1:
                return self._get_data(root.right, start, end)
            else:
                return self._get_data(root.left, start, mid) + self._get_data(root.right, mid + 1, end)

    def update_interval(self, start, end, data):
        self._update_interval(self.root, start, end, data)

    def update_single(self, idx, data):
        self._update_single(self.root, idx, data)

    def get_data(self, start, end):
        return self._get_data(self.root, start, end)


class Solution:
    _MOD = 1000000007

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
                T.update_single(idx, value)
                # print("更新区间:", (idx, idx), "=", value)

            # 第2种操作：给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin
            elif operation[0] == 2:
                idx = self.dict[operation[1]]
                l, r = self.tree[idx].start, self.tree[idx].end
                value = operation[2]
                T.update_interval(l, r, value)
                # print("更新区间:", (l, r), "=", value)
                # print([T.query(i, i) for i in range(n)], T.query(0, n - 1))

            # 第3种操作：查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和
            else:
                idx = self.dict[operation[1]]
                l, r = self.tree[idx].start, self.tree[idx].end
                ans.append(T.get_data(l, r) % self._MOD)
                # print("查询区间:", (l, r), "=", T.get_data(l, r) % 1000000007)

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
```

