# LeetCode题解(1299)：将每个元素替换为右侧最大元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 84ms (98.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def replaceElements(self, arr: List[int]) -> List[int]:
    now = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], now = now, max(now, arr[i])
    return arr
```