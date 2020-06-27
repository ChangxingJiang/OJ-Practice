# LeetCode题解(0278)：寻找第一个错误的版本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/first-bad-version/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(logn)    | O(1)       | 40ms (61.99%) |
| Ans 2 (Python) | O(logn)    | O(1)       | 36ms (83.47%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（二分法查找）：

```python
def firstBadVersion(self, n):
    left, right = 0, n
    while (right - left) > 1:
        binery = left + (right - left) // 2
        binery_ans = isBadVersion(binery)
        if binery_ans:
            right = binery
        else:
            left = binery
    return right
```

解法二（另一种二分查找）：

```python
def firstBadVersion(self, n):
    left, right = 0, n
    while right > left:
        binery = left + (right - left) // 2
        binery_ans = isBadVersion(binery)
        if binery_ans:
            right = binery
        else:
            left = binery + 1
    return left
```