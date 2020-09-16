# LeetCode题解(0456)：132模式(Python)

题目：[原题链接](https://leetcode-cn.com/problems/132-pattern/)（中等）

标签：栈、栈-单调栈

| 解法           | 时间复杂度          | 空间复杂度        | 执行用时       |
| -------------- | ------------------- | ----------------- | -------------- |
| Ans 1 (Python) | 最坏情况 : $O(N^2)$ | 最快情况 : $O(N)$ | 8444ms (5.13%) |
| Ans 2 (Python) | $O(N)$              | $O(N)$            | 184ms (69.43%) |
| Ans 3 (Python) | $O(N)$              | $O(N)$            | 168ms (94.87%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def find132pattern(self, nums: List[int]) -> bool:
    stack = []  # 需要2列表
    now = None
    for n in nums:
        for s in stack:
            if s[0] < n < s[1]:
                return True

        if now is None:
            now = n
        elif n < now:
            now = n
        elif n > now:
            for i in range(len(stack) - 1, -1, -1):
                s = stack[i]
                if now <= s[0] < s[1] <= n:
                    stack.pop(i)
            stack.append([now, n])

    return False
```

解法二（单调栈）：

```python
def find132pattern(self, nums: List[int]) -> bool:
    # 生成当前之前最小值表
    min_lst = []
    now = float("inf")
    for n in nums:
        if n < now:
            now = n
        min_lst.append(now)

    # 从后向前遍历，维护单调栈
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        # 移除栈内小于当前最小值的值
        while stack and stack[-1] <= min_lst[i]:
            stack.pop()

        # 判断是否已有解
        if stack and nums[i] > stack[-1]:
            return True

        # 更新栈
        elif not stack or nums[i] < stack[-1]:
            stack.append(nums[i])

    return False
```

解法三（更好的单调栈）：

```python
def find132pattern(self, nums: List[int]) -> bool:
    now = float("-inf")  # 当前最大的1-3-2中的2
    stack = []  # 单调栈
    for n in reversed(nums):
        if n < now:
            return True
        while stack and stack[-1] < n:
            now = stack.pop()
        stack.append(n)
    return False
```