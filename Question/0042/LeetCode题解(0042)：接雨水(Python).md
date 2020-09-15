# LeetCode题解(0042)：接雨水(Python)

题目：[原题链接](https://leetcode-cn.com/problems/trapping-rain-water/)（困难）

标签：双指针、栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 36ms (98.87%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 36ms (98.87%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 40ms (95.99%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

#### 解法一（两次遍历）：

```python
def trap(self, height: List[int]) -> int:
    # 统计当前下标右侧的最高值
    next_height = [0] * len(height)
    now_height = 0
    for i in range(len(height) - 1, -1, -1):
        now_height = max(now_height, height[i])
        next_height[i] = now_height

    # 统计可接雨水总量
    ans = 0
    now_height = 0
    for i in range(len(height)):
        now_height = max(now_height, height[i])
        ans += min(now_height, next_height[i]) - height[i]
    return ans
```

#### 解法二（双指针一次遍历）：

```python
def trap(self, height: List[int]) -> int:
    # 处理特殊情况
    if not height:
        return 0

    left = 0  # 左侧指针
    right = len(height) - 1  # 右侧指针
    left_height = height[left]  # 左侧最高高度
    right_height = height[right]  # 右侧最高高度

    ans = 0
    while left < right:
        if left_height <= right_height:
            left += 1
            left_height = max(left_height, height[left])
            ans += left_height - height[left]
        else:
            right -= 1
            right_height = max(right_height, height[right])
            ans += right_height - height[right]

    return ans
```

#### 解法三（单调栈）：

```python
def trap(self, height: List[int]) -> int:
    stack = []
    ans = 0
    for i in range(len(height)):
        if stack and height[stack[-1]] < height[i]:  # 当前高度高于栈顶高度
            last = stack.pop()  # 获取当前栈顶高度
            while stack:
                now = stack[-1]
                ans += (min(height[i], height[now]) - height[last]) * (i - now - 1)
                if height[now] < height[i]:
                    stack.pop()
                    last = now
                else:
                    break
        if not stack or height[stack[-1]] > height[i]:  # 当前栈为空或当前高度低于栈顶高度
            stack.append(i)
        if stack and height[stack[-1]] == height[i]:  # 当前高度等于栈顶高度
            stack.pop()
            stack.append(i)
    return ans
```

代码逻辑调整：

```python
def trap(self, height: List[int]) -> int:
    stack = []
    ans = 0
    for i in range(len(height)):
        while stack and height[stack[-1]] <= height[i]:
            last = stack.pop()  # 取出当前栈顶高度
            if not stack:
                break
            else:
                ans += (min(height[i], height[stack[-1]]) - height[last]) * (i - stack[-1] - 1)
        stack.append(i)
    return ans
```