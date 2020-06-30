# LeetCode题解(0599)：两个列表的最小索引总和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 328ms (29.32%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 168ms (99.58%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    min_mum = float("inf")
    min_name = []
    for i in range(len(list1)):
        n = list1[i]
        if n in list2:
            t = list2.index(n) + i
            if t < min_mum:
                min_mum = t
                min_name = [n]
            elif t == min_mum:
                min_name.append(n)
    return min_name
```

解法二（哈希表）：

```python
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    hashmap = {}
    min_mum = float("inf")
    min_name = []
    for i in range(len(list1)):
        hashmap[list1[i]] = i
    for i in range(len(list2)):
        n = list2[i]
        if n in hashmap:
            t = hashmap[n] + i
            if t < min_mum:
                min_mum = t
                min_name = [n]
            elif t == min_mum:
                min_name.append(n)
    return min_name
```