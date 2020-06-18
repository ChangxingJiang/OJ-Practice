# LeetCode精讲(0198)：计算数组中不相邻组合的最大和(Python)

## 题目内容

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 示例 1：

```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

示例 2：

```
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

提示：

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 400`

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/house-robber
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 解法效率

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 超出时间限制   |
| Ans 2 (Python) | 32ms (>96.24%) |
| Ans 3 (Python) | 40ms (>68.74%) |

> LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

#### 解法一（动态规划）：

> **【思路】** 简单思考，得到如下思路：
>
> 如果想取得最大值，那数组中每两个相邻的取值之间，只可能间隔1个数或2个数，开头有两种选择，从第一个数开始取和从第二个数开始取。
>
> 所以如果在取得第i个数，此时其最大值只能来自：取得第i-2个数的最大值再加第i个数、取得第i-3个数的最大值再加第i个数。
>
> 又有当i=0时，最大值为nums[0]；当i=1时，最大值为nums[1]；当i=2时，最大值为nums[0]+nums[2]；当i>=3时，可使用上一段的方法计算。
>
> 最终数列取得的最大值为取得nums[-1]和取得nums[-2]的两个最大值中更大的那一个。
>
> 由此得出如下初步的逻辑（这要真能运行也会慢死）：

```python
def rob(self, nums: List[int]) -> int:
    def helper(i):
        if i == 0:
            return nums[0]
        elif i == 1:
            return nums[1]
        elif i == 2:
            return nums[0] + nums[2]
        else:
            return max(helper(i - 2), helper(i - 3)) + nums[i]

    size = len(nums)
    if size == 0:
        return 0
    elif size == 1:
        return nums[0]
    else:
        return max(helper(size - 1), helper(size - 2))
```

#### 解法二（滚动数组）：

> 【思路】对以上算法进行优化，改用滚动数组的方法，将其空间复杂度优化为O(1)，时间复杂度优化为O(n)。

```python
def rob(self, nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        return 0
    elif size == 1:
        return nums[0]
    elif size == 2:
        return max(nums[0], nums[1])
    else:
        sum_1 = nums[0]  # 取得第i-3个数的最大值
        sum_2 = nums[1]  # 取得第i-2个数的最大值
        sum_3 = nums[0] + nums[2]  # 取得第i-1个数的最大值
        for i in range(3, size):
            n = nums[i]
            sum_4 = max(sum_1 + n, sum_2 + n)  # 取得第i个数的最大值
            sum_1 = sum_2
            sum_2 = sum_3
            sum_3 = sum_4
        return max(sum_2, sum_3)
```

#### 解法三（更简单的思路）：

> 【思路】此时，我们还有一个更简单的思路：
>
> 我们可以不再考虑取得某个数时的最大值，改为考虑截止到某个数的最大值。
>
> 此时，如果我们取得的某两个数（第i个数和第i+3个数）之间间隔了2个数，那么说明截止到第i个数的最大值和截止到第i+1个数的最大值是相同的。
>
> 因此，当我们改为考虑截止到某个数的最大值时，截止到第i个数的最大值只可能来自：截止到第i-2个数的最大值加第i个数、截止到第i-1个数的最大值。
>
> 由此如下的逻辑：

```python
def rob(self, nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        return 0
    elif size == 1:
        return nums[0]
    else:
        sum_1 = nums[0]
        sum_2 = max(nums[0], nums[1])
        for i in range(2, size):
            sum_3 = max(sum_1 + nums[i], sum_2)
            sum_1 = sum_2
            sum_2 = sum_3
        return max(sum_1, sum_2)
```