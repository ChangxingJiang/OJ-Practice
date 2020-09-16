# LeetCode题解(0503)：下一个更大的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/next-greater-element-ii/)（中等）

标签：栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 260ms (80.64%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

```python
def nextGreaterElements(self, nums: List[int]) -> List[int]:
    size = len(nums)
    nums += nums
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        stack.append(nums[i])
        nums[i] = stack[-2] if len(stack) > 1 else -1
    return nums[:size]
```