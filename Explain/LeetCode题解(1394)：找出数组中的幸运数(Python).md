# LeetCode题解(1394)：找出数组中的幸运数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/)（简单）

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N)$     | 64ms (62.67%) |
| Ans 2 (Python) | $O(N)$       | $O(N)$     | 64ms (62.67%) |
| Ans 3 (Python) |              |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表+排序）：

```python
def findLucky(self, arr: List[int]) -> int:
    count = collections.Counter(arr)
    for key in sorted(count.keys(), reverse=True):
        if key == count[key]:
            return key
    else:
        return -1
```

解法二（哈希表）：

```python
def findLucky(self, arr: List[int]) -> int:
    count = collections.Counter(arr)
    ans = -1
    for key, value in count.items():
        if key == value:
            ans = max(ans, key)
    return ans
```