# LeetCode题解(0658)：找到K个最接近的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-k-closest-elements/)（中等）

标签：二分查找

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时     |
| -------------- | ----------- | ---------- | ------------ |
| Ans 1 (Python) | $O(logN+K)$ | $O(K)$     | 76ms(45.91%) |
| Ans 2 (Python) |             |            |              |
| Ans 3 (Python) |             |            |              |

解法一：

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i2 = bisect.bisect_right(arr, x)
        i1 = i2 - 1
        print(i1, i2)
        ans = collections.deque()
        while len(ans) < k:
            if i1 < 0:
                ans.append(arr[i2])
                i2 += 1
            elif i2 == len(arr):
                ans.appendleft(arr[i1])
                i1 -= 1
            elif x - arr[i1] <= arr[i2] - x:
                ans.appendleft(arr[i1])
                i1 -= 1
            elif i2 < len(arr):
                ans.append(arr[i2])
                i2 += 1
        return list(ans)
```

