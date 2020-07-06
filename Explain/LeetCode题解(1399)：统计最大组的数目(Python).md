# LeetCode题解(1399)：统计最大组的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-largest-group/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 88ms (85.88%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def countLargestGroup(self, n: int) -> int:
    def helper(k):
        a = 0
        while k:
            a += k % 10
            k = k // 10
        return a

    hashmap = {}
    for i in range(1, n + 1):
        m = helper(i)
        if m in hashmap:
            hashmap[m] += 1
        else:
            hashmap[m] = 1

    maximum = max(hashmap.values())
    ans = 0
    for key, values in hashmap.items():
        if values == maximum:
            ans += 1
    return ans
```