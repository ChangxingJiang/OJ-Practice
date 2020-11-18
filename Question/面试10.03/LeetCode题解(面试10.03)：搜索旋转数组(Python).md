# LeetCode题解(面试10.03)：搜索旋转数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/search-rotate-array-lcci/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (56.75%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (78.90%) |
| Ans 3 (Python) |            |            |               |

解法一（二分查找）：

```python
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        size = len(arr)

        # 二分查找旋转位置
        aim = arr[0]
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > aim:
                left = mid + 1
            elif arr[mid] < aim:
                right = mid

            # 处理重复值的问题
            elif right - 1 > 0 and arr[right - 2] > arr[right - 1]:
                left = right - 1
                break
            else:
                right -= 1
        move = left

        # print("偏移量:", move)

        # 二分查找目标值
        ans = -1
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            actual_mid = (mid + move) % size
            # print(left, right, "->", mid, "->", actual, "=", arr[actual])
            if arr[actual_mid] < target:
                left = mid + 1
            elif arr[actual_mid] > target:
                right = mid

            # 处理最终结果是针对实际坐标
            else:
                if ans == -1 or ans > actual_mid:
                    ans = actual_mid
                actual_right = (right + move) % size
                if arr[actual_right] == target:
                    if actual_right < actual_mid:
                        return 0
                    else:
                        right = mid
                else:
                    right -= 1

        return ans
```

解法二（折腾这么多，到底测试用例会不会奖励我）：

```python
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target in arr:
            return arr.index(target)
        else:
            return -1
```