# LeetCode题解(0895)：最大频率栈(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-frequency-stack/)（困难）

标签：栈、设计、哈希表

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | push = $O(1)$ ; pop = $O(NlogN)$ | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | push = $O(1)$ ; pop = $O(1)$     | $O(N)$     | 384ms (49.62%) |
| Ans 3 (Python) |                                  |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
class FreqStack:
    def __init__(self):
        self.count = collections.Counter()
        self.stack = []

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.stack.append(x)

    def pop(self) -> int:
        # 计算所有最频繁的元素
        most_common = self.count.most_common()
        maybe_ans = [most_common[0][0]]
        now_max = most_common[0][1]
        idx = 1
        while idx < len(most_common):
            if most_common[idx][1] == now_max:
                maybe_ans.append(most_common[idx][0])
                idx += 1
            else:
                break

        # 计算最靠近栈顶的元素
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in maybe_ans:
                self.count[self.stack[i]] -= 1
                return self.stack.pop(i)
```

解法二（双层栈）：

```python
class FreqStack:
    def __init__(self):
        self.count = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.max_freq = max(self.max_freq, self.count[x])
        self.stack[self.count[x]].append(x)

    def pop(self) -> int:
        ans = self.stack[self.max_freq].pop()
        if len(self.stack[self.max_freq]) == 0:
            self.max_freq -= 1
        self.count[ans] -= 1
        return ans
```