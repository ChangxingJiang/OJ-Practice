# LeetCode题解(0621)：计算需要冷却时间的CPU任务调度器的最短运行时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/task-scheduler/)（中等）

标签：哈希表、数学、贪心算法

| 解法           | 时间复杂度                     | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(Time)$ : 其中Time为最终结果 | $O(1)$     | 284ms (16.18%) |
| Ans 2 (Python) | $O(N)$ : 其中N为任务列表长度   | $O(1)$     | 48ms (99.42%)  |
| Ans 3 (Python) |                                |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def leastInterval(self, tasks: List[str], n: int) -> int:
    count = collections.Counter(tasks)
    ans = 0
    while True:
        now = 0
        for elem in count.most_common(n + 1):
            if elem[1] > 0:
                count[elem[0]] -= 1
                now += 1
            else:
                break
        if count.most_common(1)[0][1] == 0:
            return ans + now
        ans += max(now, n + 1)
```

解法二（数学）：

![LeetCode题解(0621)：截图1](LeetCode题解(0621)：截图1.png)

```python
def leastInterval(self, tasks: List[str], n: int) -> int:
    count = collections.Counter(tasks).values()
    total = 0
    max_value = 0
    max_num = 0
    for c in count:
        total += c
        if c > max_value:
            max_value = c
            max_num = 1
        elif c == max_value:
            max_num += 1
    return max((max_value - 1) * (n + 1) + max_num, total)
```