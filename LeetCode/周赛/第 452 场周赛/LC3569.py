import collections
from typing import Callable, List, Optional

from sortedcontainers import SortedList


def sieve(n):
    """质数筛"""

    # 创建一个布尔数组，初始都为 True（True 表示是质数）
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # 将 i 的倍数全部标记为非质数
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 返回所有为 True 的下标，即质数
    return {i for i, val in enumerate(is_prime) if val}


# 计算 10 万以内所有质数的集合
prime_set = sieve(100000)


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


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # 初始化状态
        prime_hash = collections.defaultdict(lambda: SortedList())  # 每个质数的下标列表
        for i in range(n):
            num = nums[i]
            if num in prime_set:
                prime_hash[num].add(i)

        prefix_list = []  # 前缀不同质数数量
        visited_prime_set = set()
        prefix = 0
        for i in range(n):
            num = nums[i]
            if num in prime_set and num not in visited_prime_set:
                prefix += 1
                visited_prime_set.add(num)
            prefix_list.append(prefix)

        suffix_list = []  # 后缀不同质数数量
        visited_prime_set = set()
        suffix = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in prime_set and num not in visited_prime_set:
                suffix += 1
                visited_prime_set.add(num)
            suffix_list.append(suffix)
        suffix_list.reverse()

        # 初始化起始列表
        total_list = []
        for i in range(n - 1):
            total_list.append(prefix_list[i] + suffix_list[i + 1])

        # 初始化线段树
        sg = SegmentTree(n - 1,
                         update_fn_1=lambda x, y: x + y,
                         update_fn_2=lambda x, y, z: x + y,
                         query_fn=max,
                         default_list=total_list)
        # print("total_list:", total_list)

        result = []
        for idx, new_val in queries:
            old_val = nums[idx]

            # 更新质数序列和最终结果

            if old_val != new_val:

                # 旧值为质数
                if old_val in prime_set:
                    sorted_list = prime_hash[old_val]
                    i1 = sorted_list.bisect_left(idx)

                    # 左侧没有值，影响前缀和
                    if i1 == 0:
                        v1 = sorted_list[i1]

                        # 右侧没有值
                        if i1 + 1 == len(sorted_list):
                            if v1 <= n - 2:
                                # print(f"减: {v1}, {n - 2}")
                                sg.update(v1, n - 2, -1)  # 右侧前缀和全部减

                        # 右侧有值，区间减
                        else:
                            v2 = sorted_list[i1 + 1]
                            # print(f"减: {v1}, {v2 - 1}")
                            sg.update(v1, v2 - 1, -1)  # 右侧前缀和前部减

                    # 右侧没有值，影响后缀和
                    if i1 == len(sorted_list) - 1:
                        v2 = sorted_list[i1]

                        # 左侧没有值
                        if i1 == 0:
                            if v2 - 1 >= 0:
                                # print(f"减: {0}, {v2 - 1}")
                                sg.update(0, v2 - 1, -1)  # 左侧前缀和前部减

                        # 左侧有值
                        else:
                            v1 = sorted_list[i1 - 1]
                            # print(f"减: {v1}, {v2 - 1}")
                            sg.update(v1, v2 - 1, -1)  # 区间减

                    # 移除这个值
                    sorted_list.remove(idx)

                # 新值为质数
                if new_val in prime_set:
                    sorted_list = prime_hash[new_val]
                    sorted_list.add(idx)

                    i1 = sorted_list.bisect_left(idx)

                    # 新插入节点在最左侧
                    if i1 == 0:
                        v1 = sorted_list[i1]
                        # 右侧没有值
                        if i1 + 1 == len(sorted_list):
                            if v1 <= n - 2:
                                sg.update(v1, n - 2, 1)  # 右侧前缀和全部减

                        # 右侧有值，区间减
                        else:
                            v2 = sorted_list[i1 + 1]
                            sg.update(v1, v2 - 1, 1)  # 右侧前缀和前部减

                    if i1 == len(sorted_list) - 1:
                        v2 = sorted_list[i1]

                        # 左侧没有值
                        if i1 == 0:
                            if v2 - 1 >= 0:
                                sg.update(0, v2 - 1, 1)  # 左侧前缀和前部减

                        # 左侧有值
                        else:
                            v1 = sorted_list[i1 - 1]
                            sg.update(v1, v2 - 1, 1)  # 区间减

            # 更新数组
            nums[idx] = new_val

            # 查询结果
            # print("列表:", [sg.query(i, i) for i in range(n - 1)])
            result.append(sg.query(0, n - 2))

        return result


if __name__ == "__main__":
    print(Solution().maximumCount(nums=[2, 1, 3, 1, 2], queries=[[1, 2], [3, 3]]))  # [3,4]
    print(Solution().maximumCount(nums=[2, 1, 4], queries=[[0, 1]]))  # [0]

    # 测试用例
    print(Solution().maximumCount(nums=[6, 89], queries=[[0, 2], [0, 33]]))  # [2, 1]
    print(Solution().maximumCount(nums=[2, 34], queries=[[1, 2], [1, 3]]))  # [2, 2]
    print(Solution().maximumCount(nums=[96, 11, 3, 11, 2],
                                  queries=[[4, 4], [2, 19], [1, 11], [1, 9], [1, 93]]))  # [3,3,3,2,2]
