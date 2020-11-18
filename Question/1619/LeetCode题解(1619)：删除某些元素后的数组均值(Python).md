# LeetCode题解(1619)：删除某些元素后的数组均值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements/)（简单）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (45%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        size = len(arr)
        remove = size // 20  # 需要移除的数量
        arr.sort()
        return sum(arr[remove:-remove]) / (size - remove * 2)
```