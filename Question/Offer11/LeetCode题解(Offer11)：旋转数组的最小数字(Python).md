# LeetCode题解(Offer11)：旋转数组的最小数字(存在重复值)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)（简单）

标签：数组、二分查找

| 解法           | 时间复杂度                                           | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 平均时间复杂度 = $O(logN)$ ; 最坏时间复杂度 = $O(N)$ | $O(1)$     | 44ms (55.71%) |
| Ans 2 (Python) |                                                      |            |               |
| Ans 3 (Python) |                                                      |            |               |

解法一（二分查找）：

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1

        return numbers[left]
```