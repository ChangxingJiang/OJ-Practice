# LeetCode题解(0372)：超级次方(Python)

题目：[原题链接](https://leetcode-cn.com/problems/super-pow/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(A×B)$   | $O(B)$     | 176ms (27.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 1337

    def single_pow(self, a, k):
        if k == 0:
            return 1

        a %= self._MOD
        if k % 2 == 1:
            return a * self.single_pow(a, k - 1) % self._MOD
        else:
            res = self.single_pow(a, k // 2)
            return (res * res) % self._MOD

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        return self.single_pow(a, last) * self.single_pow(self.superPow(a, b), 10) % self._MOD
```

