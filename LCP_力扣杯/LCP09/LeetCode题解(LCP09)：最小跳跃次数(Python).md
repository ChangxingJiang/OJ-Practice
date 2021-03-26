# LeetCode题解(LCP09)：最小跳跃次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu/)（困难）

标签：动态规划、广度优先搜索、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(NlogN)$ | 超出时间限制   |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 324ms (98.50%) |
| Ans 3 (Python) |            |            |                |

解法一（线段树）：

```python
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
```

解法二（广度优先搜索）：

```python
class Solution:
    def minJump(self, jump: List[int]) -> int:
        size = len(jump)

        queue = collections.deque([0])
        step = 0  # 当前的步数

        visited = 0  # 当前已经访问到的位置
        while queue:
            # 累加当前步数
            step += 1

            # 处理当前广度优先搜索层
            for _ in range(len(queue)):
                n1 = queue.popleft()

                # 添加弹簧的终点
                n2 = n1 + jump[n1]
                if n2 >= size:
                    return step
                if n2 > visited:
                    queue.append(n2)

                # 向后的部分
                if n1 > visited:
                    for n2 in range(visited + 1, n1):
                        queue.append(n2)
                    visited = n1
```

