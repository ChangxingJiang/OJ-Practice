# LeetCode题解(0862)：数组中和至少为K的最短子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/)（困难）

标签：队列、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1256ms (28.05%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 996ms (74.39%)  |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（滑动窗口）：

```Python
def shortestSubarray(self, A: List[int], K: int) -> int:
    N = len(A)

    # 计算前序和
    B = [0]  # 前序和
    for n in A:
        B.append(B[-1] + n)

    #  移动窗口计算最小值
    ans = N + 1
    queue = []
    for i in range(N + 1):
        n = B[i]
        while queue and n <= B[queue[-1]]:
            queue.pop()
        while queue and n - B[queue[0]] >= K:
            t = queue.pop(0)
            ans = min(ans, i - t)
        queue.append(i)
    return ans if ans < N + 1 else -1
```

解法二（使用collections实现双端队列、使用enumerate实现遍历）：

```python
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)

        # 计算前序和
        B = [0]  # 前序和
        for n in A:
            B.append(B[-1] + n)

        #  移动窗口计算最小值
        ans = N + 1
        queue = collections.deque()
        for i,n in enumerate(B):
            while queue and n <= B[queue[-1]]:
                queue.pop()
            while queue and n - B[queue[0]] >= K:
                t = queue.popleft()
                ans = min(ans, i - t)
            queue.append(i)
        return ans if ans < N + 1 else -1
```