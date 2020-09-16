# LeetCode题解(0189)：旋转数组——所有元素向右移动(Python)

[题目链接](https://leetcode-cn.com/problems/rotate-array/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 36ms (>92.52%) |
| Ans 2 (Python) | 44ms (>65.04%) |
| Ans 3 (Python) | 40ms (>81.61%) |

解法一（直接的列表操作）：

```python
def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)  # 处理k超过列表长度的情况
    nums[:] = nums[-k:] + nums[:-k]
```

解法二（使用切片器的三次反转）：

> 1 2 3 4 5 6 7
>
> 4 3 2 1 5 6 7 反转前4项
>
> 4 3 2 1 7 6 5 反转后3项
>
> 5 6 7 1 2 3 4 反转所有项

```python
def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)  # 处理k超过列表长度的情况
    nums[-k:] = nums[-k:][::-1]
    nums[:-k] = nums[:-k][::-1]
    nums[:] = nums[::-1]
```

解法三（不使用切片器的三次反转）：

```python
def reverse(self, nums: List[int], start, end):
    while start < end:
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        start += 1
        end -= 1

def rotate(self, nums: List[int], k: int) -> None:
    l = len(nums)
    k %= l  # 处理k超过列表长度的情况
    self.reverse(nums, 0, l - k - 1)
    self.reverse(nums, l - k, l - 1)
    self.reverse(nums, 0, l - 1)
```