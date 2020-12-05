class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn, default=0):
        self.N = N
        self.update_fn = update_fn
        self.query_fn = query_fn
        self.default = default

        # 计算线段树的内部节点数量
        self.M = (self.N - 1) // 2 * 2 + 1

        # 计算线段树的高度
        self.H = 1
        while (1 << self.H) < (self.M + self.N):
            self.H += 1

        # 初始化数组表示的线段树（长度为内部节点数+叶子节点数）
        # 如果最后一个节点是其父节点的左节点的话，则为其多补出一个右节点，以避免超出
        self.tree = [self.default] * ((self.M + self.N) if (self.M + self.N) % 2 == 1 else (self.M + self.N + 1))

        # 初始化内部节点的lazy属性数组（长度为内部节点数）
        self.lazy = [self.default] * self.M

        # print("线段树的高度:", self.H, "线段树的内部节点数:", self.M)

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
            x = (x - 1) // 2

            # 计算当前节点仅受子节点影响的值
            self.tree[x] = self.query_fn(self.tree[x * 2 + 1], self.tree[x * 2 + 2])
            # 可能需要修改为如下内容
            # self.tree[x] = self.query_fn(self.tree[x], self.tree[x * 2 + 1], self.tree[x * 2 + 2])

            # 计算当前节点受lazy属性影响的值
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        """计算节点x到根节点之间的所有节点的lazy属性，将lazy属性中的值计算到节点值中，并将lazy属性清空

        :param x: x节点在数组中的坐标
        """
        for h in range(self.H, 0, -1):
            y = (x - 1) >> h
            # print("[线段树:PUSH]", x, "->", y, "->", (y * 2 + 1, y * 2 + 2))
            if self.lazy[y]:
                self._apply(y * 2 + 1, self.lazy[y])
                self._apply(y * 2 + 2, self.lazy[y])
                self.lazy[y] = self.default

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
        while 0 < l <= r:
            # print("[线段树:UPDATE]", l, "(" + str(l & 1 == 0) + ")", r, "(" + str(r & 1 == 1) + ")")
            if l & 1 == 0:
                self._apply(l, h)
                l += 1
            if r & 1 == 1:
                self._apply(r, h)
                r -= 1
            l = (l - 1) // 2
            r = (r - 1) // 2

        # 计算叶节点x及其祖先节点的值
        self._pull(l0)
        self._pull(r0)

    def query(self, l, r):
        """查询从L到R（开闭区间）的值"""

        # 计算L和R对应的叶节点坐标
        l += self.M
        r += self.M

        # 计算从根节点向下计算x的祖先节点的lazy属性中的值（将lazy属性中的值计算到节点中）
        self._push(l)
        self._push(r)

        # 查询指定范围的和
        ans = self.default
        while 0 < l <= r:
            # print("[线段树:QUERY]", l, "(" + str(l & 1 == 0) + ")", r, "(" + str(r & 1 == 1) + ")")
            if l & 1 == 0:
                ans = self.query_fn(ans, self.tree[l])
                l += 1
            if r & 1 == 1:
                ans = self.query_fn(ans, self.tree[r])
                r -= 1
            l = (l - 1) // 2
            r = (r - 1) // 2
        return ans



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