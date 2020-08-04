# LeetCode题解(0636)：函数的独占时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/exclusive-time-of-functions/)（中等）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 184ms (5.90%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 84ms (93.83%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用栈）：

```python
def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    ans = [0] * n
    last = 0
    stack = []
    for log in logs:
        idx, status, time = log.split(":")
        idx = int(idx)
        time = int(time)
        if status == "start":
            if stack:
                ans[stack[-1]] += time - last - 1
            stack.append(idx)
            ans[idx] += 1
            last = time
        else:
            if not stack or stack[-1] != idx:
                continue
            else:
                ans[stack[-1]] += time - last
                stack.pop()
                last = time
    return ans
```

解法二（更好的使用栈）：

```python
def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    ans = [0] * n
    stack = []
    for log in logs:
        nid, status, time = log.split(":")
        nid = int(nid)
        time = int(time)
        if status == "start":
            stack.append([nid, time])
        else:
            lid, last = stack.pop()
            interval = time - last + 1
            ans[lid] += interval
            if stack:
                ans[stack[-1][0]] -= interval
    return ans
```