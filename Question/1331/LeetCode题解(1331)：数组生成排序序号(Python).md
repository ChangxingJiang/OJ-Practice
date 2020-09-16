# LeetCode题解(1331)：数组生成排序序号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rank-transform-of-an-array/)（简单）

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N)$     | 超时时间限制   |
| Ans 2 (Python) | $O(NlogN)$   | $O(N)$     | 420ms (60.51%) |
| Ans 3 (Python) |              |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力法）：

```python
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    s = sorted(set(arr))
    return [s.index(a) + 1 for a in arr]
```

解法二（哈希表存储序号）：

```python
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    hashmap = {}
    srr = list(set(arr))
    srr.sort()
    for i in range(len(srr)):
        hashmap[srr[i]] = i + 1
    return [hashmap[a] for a in arr]
```