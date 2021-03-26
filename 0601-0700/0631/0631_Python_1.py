import collections
from typing import List


class Excel:

    def __init__(self, h: int, w: str):
        self.h = h
        self.w = self._get_col(w) + 1
        self.table = [[0] * self.w for _ in range(self.h)]
        self.formula = {}  # 公式列表（用于删除公式时使用）

        self.graph = collections.defaultdict(collections.Counter)  # 单元格关系图（用于更新值时使用）

    def set(self, r: int, c: str, v: int) -> None:
        r -= 1
        c = self._get_col(c)
        # print("[SET]", (r, c), "->", v)
        if 0 <= r < self.h and 0 <= c < self.w:
            self._update(r, c, v - self.table[r][c])  # 更新单元格的值，并更新所有引用了这个单元格的值
            self._remove(r, c)  # 移除单元格中的公式和单元格关系

    def get(self, r: int, c: str) -> int:
        r -= 1
        c = self._get_col(c)
        return self.table[r][c]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        r -= 1
        c = self._get_col(c)
        # print("[SUM]", (r, c), "->", strs)
        self.formula[(r, c)] = collections.Counter()  # 引用的单元格列表
        self.table[r][c] = 0
        for s in strs:
            if ":" not in s:
                r1, c1 = int(s[1:]) - 1, self._get_col(s[0])
                # print("[SUM]", (r, c), "<-", (r1, c1))
                self.formula[(r, c)][(r1, c1)] += 1  # 记录公式关系
                self.table[r][c] += self.table[r1][c1]  # 计算当前位置的值
                self.graph[(r1, c1)][(r, c)] += 1  # 更新单元格关系图
            else:
                s1, s2 = s.split(":")
                r1, c1 = int(s1[1:]) - 1, self._get_col(s1[0])
                r2, c2 = int(s2[1:]) - 1, self._get_col(s2[0])
                # print("[SUM]", s, "->", (r1, c1), (r2, c2))
                for r3 in range(r1, r2 + 1):
                    for c3 in range(c1, c2 + 1):
                        # print("[SUM]", (r, c), "<-", (r3, c3))
                        self.formula[(r, c)][(r3, c3)] += 1  # 记录公式关系
                        self.table[r][c] += self.table[r3][c3]  # 计算当前位置的值
                        self.graph[(r3, c3)][(r, c)] += 1  # 更新单元格关系图
        return self.table[r][c]

    def _remove(self, r: int, c: int) -> None:
        """移除单元格中的公式和单元格关系"""
        if (r, c) in self.formula:
            for r1, c1 in self.formula[(r, c)]:
                del self.graph[(r1, c1)][(r, c)]
            del self.formula[(r, c)]

    def _update(self, r: int, c: int, v: int) -> None:
        """更新单元格的值，并更新所有引用了这个单元格的值"""
        queue = collections.deque([(r, c, 1)])
        while queue:
            (r1, c1, t1) = queue.popleft()
            self.table[r1][c1] += v * t1
            # print("[UPDATE]", (r, c), "->", (r1, c1), "=", v * t1)
            if (r1, c1) in self.graph:
                for (r2, c2) in self.graph[(r1, c1)]:
                    queue.append((r2, c2, t1 * self.graph[(r1, c1)][(r2, c2)]))

    @staticmethod
    def _get_col(s: str) -> int:
        """依据列名计算列号"""
        ans = 0
        for i in range(len(s)):
            ans += (ord(s[-(i + 1)]) - 64) * pow(26, i)
        return ans - 1


if __name__ == "__main__":
    obj = Excel(3, "C")
    obj.set(1, "A", 2)
    print(obj.sum(3, "C", ["A1", "A1:B2"]))  # 4
    obj.set(2, "B", 2)
    print()

    obj = Excel(3, "C")
    print(obj.sum(1, "A", ["A2"]))  # 0
    obj.set(2, "A", 1)
    print(obj.get(1, "A"))  # 1
    print()

    obj = Excel(3, "C")
    print(obj.get(1, "A"))  # 0
    obj.set(1, "A", 1)
    obj.set(1, "A", 2)
    print(obj.get(1, "A"))  # 2

    # 下面是被简化的测试用例13
    obj = Excel(3, "C")
    obj.set(1, "A", 1)
    obj.sum(2, "B", ["A1", "A1"])
    obj.set(1, "A", 2)
    obj.sum(3, "C", ["B2", "A1:B2"])
    obj.set(2, "B", 0)
    print(obj.get(3, "C"))
    print()

    obj = Excel(26, "Z")
    obj.set(1, "A", 1)
    obj.set(1, "I", 1)
    print(obj.graph)
    print(obj.sum(7, "D", ["A1:D6", "A1:G3", "A1:C12"]))  # 3
    print(obj.graph)
    print(obj.sum(10, "G", ["A1:D7", "D1:F10", "D3:I8", "I1:I9"]))  # 11
    print(obj.graph)
