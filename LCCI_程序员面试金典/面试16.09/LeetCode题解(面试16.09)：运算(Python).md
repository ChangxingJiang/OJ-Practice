# LeetCode题解(面试16.09)：运算(Python)

题目：[原题链接](https://leetcode-cn.com/problems/operations-lcci/)（中等）

标签：设计、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 156ms (22.41%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Operations:

    def __init__(self):
        self.neg_cache = []
        self.pos_cache = []
        neg, pos = -1, 1
        for i in range(32):
            self.neg_cache.append(neg)
            self.pos_cache.append(pos)
            neg += neg
            pos += pos

    # 计算相反数
    def _minus(self, n):
        if n == 0:
            return n

        if n > 0:
            use_cache, aim_cache = self.pos_cache, self.neg_cache
        else:
            use_cache, aim_cache = self.neg_cache, self.pos_cache

        res = 0
        for i in range(31, -1, -1):
            # 处理正数
            if 0 < use_cache[i] <= n:
                res += aim_cache[i]
                n += aim_cache[i]

            # 处理负数
            elif n <= use_cache[i] < 0:
                res += aim_cache[i]
                n += aim_cache[i]
        return res

    def minus(self, a: int, b: int) -> int:
        return a + self._minus(b)

    def multiply(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        elif (a > 0 and b > 0) or (a < 0 and b < 0):
            bit = 1
        else:
            bit = -1

        if a < 0:
            a = self._minus(a)
        if b < 0:
            b = self._minus(b)

        # 计算需要乘的位
        lst = []
        for i in range(31, -1, -1):
            if self.pos_cache[i] <= b:
                lst.append(True)
                b += self.neg_cache[i]
            else:
                lst.append(False)

        # 乘对应的位
        ans = 0
        while lst:
            if lst.pop():
                ans += a
            a += a

        if bit == 1:
            return ans
        else:
            return self._minus(ans)

    def divide(self, a: int, b: int) -> int:
        if a == 0:
            return 0
        elif (a > 0 and b > 0) or (a < 0 and b < 0):
            bit = 1
        else:
            bit = -1

        if a < 0:
            a = self._minus(a)
        if b < 0:
            b = self._minus(b)

        ans_lst = list(self.pos_cache)
        val_lst = []
        for i in range(32):
            val_lst.append(b)
            b += b

        ans = 0
        while val_lst:
            v1 = ans_lst.pop()
            v2 = val_lst.pop()
            if a >= v2:
                ans += v1
                a += self._minus(v2)

        if bit == 1:
            return ans
        else:
            return self._minus(ans)
```