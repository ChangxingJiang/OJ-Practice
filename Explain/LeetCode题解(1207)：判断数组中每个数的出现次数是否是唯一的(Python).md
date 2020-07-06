# LeetCode题解(1207)：判断数组中每个数的出现次数是否是唯一的(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-number-of-occurrences/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (67.15%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def uniqueOccurrences(self, arr: List[int]) -> bool:
    count = collections.Counter(arr)
    return len(count.values()) == len(set(count.values()))
```

