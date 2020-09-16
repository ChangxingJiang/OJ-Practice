# LeetCode题解(1450)：在既定时间做作业的学生人数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/)（简单）

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(S+E+Q)$ : S为startTime的长度，E为endTime的长度，Q为querytime | $O(S+E)$   | 48ms (20.08%) |
| Ans 2 (Python) | $O(S+E)$: S为startTime的长度，E为endTime的长度               | $O(1)$     | 36ms (90.21%) |
| Ans 3 (Python) |                                                              |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    start_count = collections.Counter(startTime)
    end_count = collections.Counter(endTime)
    now = 0
    for i in range(1, queryTime + 1):
        if i in start_count:
            now += start_count[i]
        if i - 1 in end_count:
            now -= end_count[i - 1]
    return now
```

解法二（优化解法一）：

```python
def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
    ans = 0
    for start in startTime:
        if start <= queryTime:
            ans += 1
    for end in endTime:
        if end < queryTime:
            ans -= 1
    return ans
```