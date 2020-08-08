# LeetCode题解(0975)：数组里的奇偶跳游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/odd-even-jump/)（困难）

标签：栈、栈-单调栈、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(NlogN)$ | $O(N)$     | 372ms (49.02%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

> 题意即依次寻找大于等于当前值的最小值、小于等于当前值的最大值。

```python
def oddEvenJumps(self, A: List[int]) -> int:
    # 使用单调排序栈统计每一个元素奇偶跳的下一个元素
    size = len(A)
    next_odd = [-1] * size  # 奇跳的下一个元素(大于等于当前值的最小值)
    next_even = [-1] * size  # 偶跳的下一个元素(小于等于当前值的最大值)
    stack_odd = []  # 单调递减栈(用于计算奇跳)
    stack_even = []  # 单调递增栈(用于计算偶跳)
    for i in range(len(A) - 1, -1, -1):
        # 计算奇跳的下一个元素
        temp = []
        while stack_odd and A[stack_odd[-1]] < A[i]:
            temp.append(stack_odd.pop())
        if stack_odd:
            next_odd[i] = stack_odd[-1]
        if temp and A[temp[-1]] == A[i]:
            temp.pop()
        temp.append(i)
        while temp:
            stack_odd.append(temp.pop())

        # 计算偶跳的下一个元素
        temp = []
        while stack_even and A[stack_even[-1]] > A[i]:
            temp.append(stack_even.pop())
        if stack_even:
            next_even[i] = stack_even[-1]
        if temp and A[temp[-1]] == A[i]:
            temp.pop()
        temp.append(i)
        while temp:
            stack_even.append(temp.pop())

    print(next_odd, next_even)

    # 统计到达每一个元素的奇偶步数
    steps = [[1, 0] for _ in range(size)]  # 第1个为到达当前位置的该奇跳的数量，第2个为到达当前位置的该偶跳的数量
    for i in range(size):
        # 计算下一步为奇跳的情况
        if next_odd[i] != -1:
            steps[next_odd[i]][1] += steps[i][0]

        # 计算下一步为偶跳的情况
        if next_even[i] != -1:
            steps[next_even[i]][0] += steps[i][1]

    return steps[-1][0] + steps[-1][1]
```

解法二（更好的单调栈）：

```python
def oddEvenJumps(self, A: List[int]) -> int:
    # 使用单调排序栈统计每一个元素奇偶跳的下一个元素
    size = len(A)
    next_odd = [-1] * size  # 奇跳的下一个元素(大于等于当前值的最小值)
    next_even = [-1] * size  # 偶跳的下一个元素(小于等于当前值的最大值)
    stack_odd = []  # 单调递减栈(用于计算奇跳)
    stack_even = []  # 单调递增栈(用于计算偶跳)
    sorted_odd = sorted(range(size), key=lambda i: A[i])  # 递增排序
    sorted_even = sorted(range(size), key=lambda i: -A[i])  # 递减排序

    # 计算奇跳的下一个元素
    for i in reversed(sorted_odd):
        while stack_odd and stack_odd[-1] < i:
            stack_odd.pop()
        if stack_odd:
            next_odd[i] = stack_odd[-1]
        stack_odd.append(i)

    # 计算偶跳的下一个元素
    for i in reversed(sorted_even):
        while stack_even and stack_even[-1] < i:
            stack_even.pop()
        if stack_even:
            next_even[i] = stack_even[-1]
        stack_even.append(i)

    print(next_odd, next_even)

    # 统计到达每一个元素的奇偶步数
    steps = [[1, 0] for _ in range(size)]  # 第1个为到达当前位置的该奇跳的数量，第2个为到达当前位置的该偶跳的数量
    for i in range(size):
        # 计算下一步为奇跳的情况
        if next_odd[i] != -1:
            steps[next_odd[i]][1] += steps[i][0]

        # 计算下一步为偶跳的情况
        if next_even[i] != -1:
            steps[next_even[i]][0] += steps[i][1]

    return steps[-1][0] + steps[-1][1]
```