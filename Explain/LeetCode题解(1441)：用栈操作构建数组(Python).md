# LeetCode题解(1441)：用栈操作构建数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/build-an-array-with-stack-operations/)（简单）

| 解法           | 时间复杂度             | 空间复杂度 | 执行用时      |
| -------------- | ---------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$                 | $O(N)$     | 40ms (66.32%) |
| Ans 2 (Python) | $O(N)$                 | $O(N)$     | 36ms (86.88%) |
| Ans 3 (Python) | $O(T)$ : T为target长度 | $O(1)$     | 40ms (66.32%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

```python
def buildArray(self, target: List[int], n: int) -> List[str]:
    source = [i for i in range(1, n + 1)]
    ans = []
    while target and source:
        if target[0] == source[0]:
            target.pop(0)
            source.pop(0)
            ans.append("Push")
        else:
            source.pop(0)
            ans.append("Push")
            ans.append("Pop")
    return ans
```

解法二（双指针情景模拟）：

```python
def buildArray(self, target: List[int], n: int) -> List[str]:
    source = [i for i in range(1, n + 1)]
    idx1 = 0
    idx2 = 0
    ans = []
    while idx1 < len(target) and idx2 < len(source):
        if target[idx1] == source[idx2]:
            idx1 += 1
            idx2 += 1
            ans.append("Push")
        else:
            idx2 += 1
            ans.append("Push")
            ans.append("Pop")
    return ans
```

解法三：

```python
def buildArray(self, target: List[int], n: int) -> List[str]:
    ans = []
    last = 0
    for t in target:
        ans += ["Push", "Pop"] * (t - last - 1) + ["Push"]
        last = t
    return ans
```