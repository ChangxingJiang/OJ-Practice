# LeetCode题解(0594)：计算最长和谐子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-harmonious-subsequence/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 368ms (91.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def findLHS(self, nums: List[int]) -> int:
    hashmap = {}
    for n in nums:
        if n not in hashmap:
            hashmap[n] = 1
        else:
            hashmap[n] += 1
    maximum = 0
    for k in hashmap:
        if k - 1 in hashmap:
            v = hashmap[k] + hashmap[k - 1]
            if v > maximum:
                maximum = v
    return maximum
```