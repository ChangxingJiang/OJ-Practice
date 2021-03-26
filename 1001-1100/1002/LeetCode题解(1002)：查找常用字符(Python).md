# LeetCode题解(1002)：查找常用字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-common-characters/)（简单）

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时      |
| -------------- | ------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N×K)$ : K为字符串长度 | $O(K)$     | 56ms (76.09%) |
| Ans 2 (Python) | $O(N×K)$ : K为字符串长度 | $O(K)$     | 56ms (76.09%) |
| Ans 3 (Python) |                          |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def commonChars(self, A: List[str]) -> List[str]:
    hashmap = {}
    for c in A[0]:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    for a in A[1:]:
        for k in hashmap:
            hashmap[k] = min(hashmap[k], a.count1(k))

    ans = []
    for k, v in hashmap.items():
        while v > 0:
            ans.append(k)
            v -= 1

    return ans
```

解法二（使用collections.Counter类）：

```python
def commonChars(self, A: List[str]) -> List[str]:
    ans = collections.Counter(A[0])

    for a in A[1:]:
        ans &= collections.Counter(a)

    return list(ans.elements())
```