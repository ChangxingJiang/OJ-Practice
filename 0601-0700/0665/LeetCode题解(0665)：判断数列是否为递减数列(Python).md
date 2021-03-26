# LeetCode题解(0665)：判断数列是否为递减数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/non-decreasing-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (70.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（分别检查异常变大和异常变小两种情况）：

```python
def checkPossibility(self, nums: List[int]) -> bool:
    idx = 0
    wrong = False
    while idx < len(nums) - 1:
        if nums[idx] > nums[idx + 1]:
            if wrong:
                print("两次错误")
                return False
            else:
                wrong = True
                if idx > 0 and idx + 1 < len(nums) and nums[idx - 1] > nums[idx + 1]:
                    if idx + 2 < len(nums) and nums[idx] > nums[idx + 2]:
                        return False
        idx += 1
    else:
        return True
```