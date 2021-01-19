# LeetCode题解(0969)：煎饼排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pancake-sorting/)（中等）

标签：数组、排序、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 36ms (96.12%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        now_idx = len(arr) - 1

        while now_idx > 0:
            # 寻找最大值
            max_val = max(arr)

            # 最大值已经在数组末尾
            if arr[now_idx] == max_val:
                arr.pop()
                now_idx -= 1

            # 最大值还不在数组末尾
            else:
                # 将最大值移动到末尾
                max_idx = arr.index(max_val)
                ans.append(max_idx + 1)
                ans.append(now_idx + 1)

                # 更新数组和数组末尾
                arr = arr[max_idx + 1:][::-1] + arr[:max_idx]
                now_idx -= 1

        return ans
```

