# LeetCode题解(1491)：去掉最低工资和最高工资后的工资平均值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (83.26%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 32ms (95.38%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def average(self, salary: List[int]) -> float:
    return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
```

解法二：

```python
def average(self, salary: List[int]) -> float:
    sum_ = 0
    max_ = 0
    min_ = float("inf")
    for s in salary:
        sum_ += s
        max_ = max(max_, s)
        min_ = min(min_, s)
    return (sum_ - max_ - min_) / (len(salary) - 2)
```