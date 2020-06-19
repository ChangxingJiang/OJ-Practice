# LeetCode精讲(0204)：计算小于n的质数数量(Python)

## 题目内容

统计所有小于非负整数 *n* 的质数的数量。

**示例:**

```
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
```

> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/count-primes/
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 运行效率

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时        |
| -------------- | -------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(n^2)$       | $O(1)$     | 超出时间限制    |
| Ans 2 (Python) | $O(n\sqrt{n})$ | $O(1)$     | 超出时间限制    |
| Ans 3 (Python) | $O(n\sqrt{n})$ | $O(1)$     | 超出时间限制    |
| Ans 4 (Python) | $O(n^2)$       | $O(n)$     | 752ms (>37.08%) |
| Ans 5 (Python) | $O(n\sqrt{n})$ | $O(n)$     | 476ms (>53.63%) |
| Ans 6 (Python) | $O(n\sqrt{n})$ | $O(n)$     | 124ms (>89.48%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

## 解法一（完全暴力算法）：

【思路】

首先，依据质数的定义，我们得到如下算法：

遍历所有小于目标值(n)且大于等于2的整数(c)；并将这些整数(c)除以小于它们(c)且大于等于2的整数(i)来判断它们是不是质数。

这样的方法显示十分麻烦，每个数(c)都要除以c-1个数才能判断完成，此时的时间复杂度为O(n^2)。

```python
def countPrimes(self, n: int) -> int:
    def is_primes(c):
        """
        判断c是否为质数
        """
        for i in range(2, n):
            if c % i == 0:
                return False
        return True

    ans = 0
    for j in range(2, n):
        if is_primes(j):
            ans += 1
    return ans
```

## 解法二（不那么暴力的暴力算法）：

【思路】

实际上，并不需要除以所有小于等于某整数(c)的整数来判断该整数(c)是否为质数。

因为，除该整数(c)的平方根外，其他所有可以整除该整数的两个数，都是一个小于平方根，一个大于平方根。例如：` 4 < sqrt(24) < 6`

所以，当除到该整数(c)的平方根时，就已经可以将所有可能的情况枚举出来了。

由此，我们对算法优化如下：

```python
def countPrimes(self, n: int) -> int:
    def is_primes(c):
        """
        判断c是否为质数
        """
        for i in range(2, int(pow(c, 0.5)) + 1):
            if c % i == 0:
                return False
        return True

    ans = 0
    for j in range(2, n):
        if is_primes(j):
            ans += 1
    return ans
```

## 解法三（更不暴力的暴力算法）：

【思路】

在解法二的基础上，我们发现其实如果已经除了2，那么再除4、6等偶数都是没有意义的。

因此，我们将算法优化为只除以之前已经发现的质数，得到如下算法：

```python
def countPrimes(self, n: int) -> int:
    prime_list = []
    for c in range(2, n):
        for i in prime_list:
            if c % i == 0:
                break
        else:
            prime_list.append(c)
    return len(prime_list)
```

## 解法四（使用数组标记合数）：

【思路】

既然后面的数我们已经是通过之前除以之前发现的质数来判断是否为质数，那没有其实已经没有必要再继续使用耗时更高除法了。

我们可以建立一个数组，用以标记各个数是否为质数；当我们每发现一个质数，就遍历将所有该质数的倍数标记为合数；这种方法叫做“厄拉多塞筛法”。

由此，我们得到如下算法，虽然时间复杂度为O(n^2)，但是不用再使用除法了：

```python
def countPrimes(self, n: int) -> int:
    num_list = [True for _ in range(n)]

    for i in range(2, n):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            for j in range(2 * i, n, i):
                num_list[j] = False

    ans = 0
    for i in range(2, n):
        if num_list[i]:
            ans += 1
    return ans
```

## 解法五（优化解法四）：

【思路】

因为我们在标记7的倍数时，14、21、28、35、42都已经被2、3、5标记过了，即7\*7以下的7的倍数都已经被标记了，所以，我们只需要从7*7向上标记7的倍数就可以了。

因此，当我们判断到n平方根（即标记完小于等于n平方根的最大质数）后，就不用再判断和标记了。

由此，我们得到了如下算法：

```python
def countPrimes(self, n: int) -> int:
    num_list = [True for _ in range(n)]

    for i in range(2, int(pow(n, 0.5)) + 1):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            for j in range(i * i, n, i):
                num_list[j] = False

    ans = 0
    for i in range(2, n):
        if num_list[i]:
            ans += 1
    return ans
```

## 解法六（优化解法五）：

【思路】

因为在Python中，Python的内置语句往往会比我们自己写的算法要更快，因此我们更多地使用一些Python的内置语句来优化算法。

同时，在生成各元素相同的列表时，“列表生成式”的运行速度比“列表乘以常数”的运行速度要慢很多，不再使用列表生成式。

```python
def countPrimes(self, n: int) -> int:
    if n < 2:
        return 0

    num_list = [True]*n
    num_list[0], num_list[1] = False, False

    for i in range(2, int(pow(n, 0.5)) + 1):
        if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
            num_list[i * i::i] = [False] * ((n - i * i - 1) // i + 1)  # 因为要包含i*i所以需要+1；因为n不在列表里，所以需要-1

    return sum(num_list)  # True就是1，False就是0，可以直接统计
```

至此，其实我们的算法已经优化得很好了，把那些枚举LeetCode测试数据的人忽略掉就行了。