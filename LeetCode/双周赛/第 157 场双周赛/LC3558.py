from collections import defaultdict
from typing import List

MOD = 10 ** 9 + 7


class Permutation:
    def __init__(self, mod=10 ** 9 + 7):
        self._mod = mod
        self._size = 0

        self._factorial = [1]  # 阶乘缓存列表 : self.fact[i] = i!
        self._factorial_inv = [1]  # 阶乘的乘法逆元缓存列表

    def factorial(self, n):
        """计算阶乘"""
        if n > self._size:
            for i in range(self._size + 1, n + 1):
                self._factorial.append((self._factorial[-1] * i) % self._mod)
                self._factorial_inv.append(pow(self._factorial[-1], self._mod - 2, self._mod))
            self._size = n
        return self._factorial[n]

    def arrange(self, n, m):
        """排列数公式(n>=m)"""
        a_mod = self.factorial(n)
        b_mod = self.factorial(n - m)
        inv_b = pow(b_mod, -1, self._mod)
        return (a_mod * inv_b) % self._mod

    def comb(self, n, m):
        """组合数公式(n>=m)"""
        a_mod = self.arrange(n, m)
        b_mod = self.factorial(m)
        inv_b = pow(b_mod, -1, self._mod)
        return (a_mod * inv_b) % self._mod


permutation = Permutation(mod=MOD)


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # 计算树的最大深度
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        queue = [1]
        visited = {1}
        depth = 0  # 深度为路径数 + 1
        while queue:
            depth += 1
            new_queue = []
            for u in queue:
                for v in tree[u]:
                    if v not in visited:
                        new_queue.append(v)
                        visited.add(v)
            queue = new_queue

        # 计算赋值方式数量
        path = depth - 1  # depth >= 2 and path >= 1
        if path % 2 == 0:  # 偶数，从 C0n 开始
            result = 0
            for i in range(0, path + 1, 2):
                result = (result + permutation.comb(path, i)) % MOD
            return result
        else:  # 奇数，从 C1n 开始
            result = 0
            for i in range(1, path + 1, 2):
                result = (result + permutation.comb(path, i)) % MOD
            return result


if __name__ == "__main__":
    print(Solution().assignEdgeWeights([[1, 2]]))  # 1
    print(Solution().assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))  # 2
    print(Solution().assignEdgeWeights([[3, 2], [2, 1]]))  # 2
