# LeetCode精讲(0581)：数组中的最短无序连续子数组(Python)

## 题目内容

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

**示例 1：**

```
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
```

**说明：**

* 输入的数组长度范围在 [1, 10,000]。

* 输入的数组可能包含重复元素 ，所以升序的意思是<=。

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray

## 解法效率

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 3 (Python) | $O(N^2)$   | $O(1)$     | 超出时间限制   |
| Ans 4 (Python) | $O(NlogN)$ | $O(N)$     | 268ms (61.40%) |
| Ans 5 (Python) | $O(NlogN)$ | $O(N)$     | 232ms (98.99%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（暴力的栈实现）：

> 【思路】
>
> 使用栈存储当前遍历的数组，如果发现新的数(n)比栈顶元素小，记录栈顶的坐标作为排序数组的结束坐标(reverse_max_idx)；从栈中不断取出元素，直到取出的元素比该数(n)大或达到栈底，此时的坐标即为排序数组的起始坐标(reverse_min_idx)；再将取出的元素升序放回栈中（可用另一个栈实现）。
>
> 排序数组的起始坐标一旦被确定，就不再更改；而排序数组的结束坐标，则不断更新。最终的结果即为排序树组的结束坐标减去起始坐标。
>
> 这种方法一直在维护一个升序的栈，但如果整个数组是一个倒序的数组，则会有巨大的时间复杂度。

```python
def findUnsortedSubarray(self, nums: List[int]) -> int:
    stack = []
    reverse_min_idx = None
    reverse_max_idx = None
    for i in range(len(nums)):
        n = nums[i]
        if len(stack) == 0 or n >= stack[-1]:
            stack.append(n)
        else:
            reverse_end_idx = i
            reverse_start_idx = i

            # 使用临时栈到倒序部分升序
            temp_stack = []
            while len(stack) > 0 and n < stack[-1]:
                reverse_start_idx -= 1
                temp_stack.append(stack.pop(-1))
            temp_stack.append(n)

            while temp_stack:
                stack.append(temp_stack.pop(-1))

            # 更新升序数组起始坐标和升序数组结尾坐标
            if reverse_min_idx is None or reverse_start_idx < reverse_min_idx:
                reverse_min_idx = reverse_start_idx
            if reverse_max_idx is None or reverse_end_idx > reverse_max_idx:
                reverse_max_idx = reverse_end_idx

    if reverse_min_idx is not None and reverse_max_idx is not None:
        return reverse_max_idx - reverse_min_idx + 1
    else:
        return 0
```

### 解法二（暴力的维护最大值数组）：

> **【思路】**
>
> 解法一中，我们发现实际上我们需要维护完整的升序数组，只需要维护最大值数组即可。
>
> 但是，这种方法和解法一拥有相似的时间复杂度，这种方法仍然无法解决倒序数组时间复杂度过大的问题。

```python
def findUnsortedSubarray(self, nums: List[int]) -> int:
    max_list = [-1] * len(nums)
    reverse_min_idx = None
    reverse_max_idx = None

    for i in range(len(nums)):
        if (i > 0 and nums[i] >= max_list[i - 1]) or i == 0:
            max_list[i] = nums[i]
        else:
            # 维护最大值数组
            max_list[i] = max_list[i - 1]

            # 计算起始坐标
            idx = i - 1
            while idx >= 0 and max_list[idx] > nums[i]:
                idx -= 1
            idx += 1

            # 更新升序数组起始坐标和升序数组结尾坐标
            if reverse_min_idx is None or idx < reverse_min_idx:
                reverse_min_idx = idx
            if reverse_max_idx is None or i > reverse_max_idx:
                reverse_max_idx = i

    if reverse_min_idx is not None and reverse_max_idx is not None:
        return reverse_max_idx - reverse_min_idx + 1
    else:
        return 0
```

### 解法三（暴力的两层循环）：

> **【思路】**
>
> 通过解法一和解法二我们发现，与其使用O(N^2)的时间复杂度来维护一个升序栈或一个最大值数组，还不如直接用O(N^2)的时间复杂度来比较数组中所有数之间的大小，仅维护需升序数组的起始坐标(reverse_min_idx)和结束坐标(reverse_max_idx)。
>
> 我们比较数组中每两个数组的大小，如果发现左边的比右边的大，那么就判断是否需要更新起始坐标(reverse_min_idx)和结束坐标(reverse_max_idx)。
>
> 但是这种方法的时间复杂度仍然是O(N^2)。

```python
def findUnsortedSubarray(self, nums: List[int]) -> int:
    reverse_min_idx = len(nums) - 1
    reverse_max_idx = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                reverse_min_idx = min(reverse_min_idx, i)
                reverse_max_idx = max(reverse_max_idx, j)

    if reverse_min_idx > reverse_max_idx:
        return 0
    else:
        return reverse_max_idx - reverse_min_idx + 1
```

### 解法四（排序）：

> **【思路】**
>
> 我们想到与其分别比较所有数组，还不如直接将数组排序；比较原数组和排序后数组不同之处的最小坐标和最大坐标，这些坐标也就是需要升序数组的起始坐标和结束坐标。
>
> 这种方法的时间复杂度为排序的O(NlogN)和排序后遍历的O(N)，时间复杂度大幅度下降。

```python
def findUnsortedSubarray(self, nums: List[int]) -> int:
    minimum = len(nums) - 1
    maximum = 0
    sorts = sorted(nums)
    for i in range(len(nums)):
        if sorts[i] != nums[i]:
            minimum = min(minimum, i)
            maximum = max(maximum, i)

    return maximum - minimum + 1 if minimum < maximum else 0
```

### 解法五（解法四的优化）：

> **【思路】**
>
> 我们再在解法四的基础上做一个小小的优化，在遍历时不再完整遍历，而是从前往后、从后往前分别找到第一个存在差异的点即可。

```python
def findUnsortedSubarray(self, nums: List[int]) -> int:
    sorts = sorted(nums)
    for i in range(len(nums)):
        if sorts[i] != nums[i]:
            minimum = i
            break
    else:
        return 0
    for i in range(len(nums) - 1, -1, -1):
        if sorts[i] != nums[i]:
            maximum = i
            break
    else:
        return 0
    return maximum - minimum + 1
```