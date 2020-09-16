# LeetCode题解(1346)：检查整数及其两倍数是否存在(Python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-n-and-its-double-exist/)（简单）

第0001题的扩展

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (90.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def checkIfExist(self, arr: List[int]) -> bool:
    hashmap = set()
    for n in arr:
        if n * 2 in hashmap or n / 2 in hashmap:
            return True
        else:
            hashmap.add(n)
    else:
        return False
```