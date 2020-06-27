# LeetCode题解(0283)：将数组中的零移动到数组结尾(Python)

题目：[原题链接](https://leetcode-cn.com/problems/move-zeroes/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(n^2)$   | O(1)       | 460ms (5.71%) |
| Ans 2 (Python) | O(n)       | O(n)       | 40ms (85.03%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（两层迭代）：

```python
def moveZeroes(self, nums: List[int]) -> None:
    size = len(nums)
    i = 0
    zero = 0
    while i + zero < size:
        n = nums[i]
        if n == 0:
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j + 1]
            nums[-1] = 0
            zero += 1
        else:
            i += 1
```

解法二（数组存储非0位）：

```python
def moveZeroes(self, nums: List[int]) -> None:
    sites = []
    for i in range(len(nums)):
        n = nums[i]
        if n != 0:
            sites.append(n)

    index = 0
    for n in sites:
        nums[index] = n
        index += 1

    for i in range(len(sites), len(nums)):
        nums[i] = 0
```

