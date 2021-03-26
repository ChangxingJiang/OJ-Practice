# LeetCode题解(Offer62)：不断删除圆圈中的第m个数字求最后剩下的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)（简单）

标签：数学、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 240ms (54.71%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 80ms (97.26%)  |
| Ans 3 (Python) |            |            |                |

解法一（递归）：

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 处理n==0的情况
        if n == 0:
            return 0

        # 处理n>0的情况
        else:
            return (self.lastRemaining(n - 1, m) + m) % n
```

解法二（迭代）：

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        val = 0
        for i in range(1, n + 1):
            val = (val + m) % i
        return val
```