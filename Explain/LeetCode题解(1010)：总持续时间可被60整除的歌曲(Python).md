# LeetCode题解(1010)：总持续时间可被60整除的歌曲(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 264ms (92.32%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力方法，直接枚举求余）：

```python
def numPairsDivisibleBy60(self, time: List[int]) -> int:
    ans = 0
    for pair in itertools.combinations(time, 2):
        if (pair[0] + pair[1]) % 60 == 0:
            ans += 1
    return ans
```

解法二（更好的暴力，先求余再枚举）：

```python
def numPairsDivisibleBy60(self, time: List[int]) -> int:
    time = [t % 60 for t in time]
    ans = 0
    for pair in itertools.combinations(time, 2):
        remainder = pair[0] + pair[1]
        if remainder == 0 or remainder == 60:
            ans += 1
    return ans
```

解法三：

```python
def numPairsDivisibleBy60(self, time: List[int]) -> int:
    count = collections.Counter([t % 60 for t in time])
    ans = 0
    if 0 in count:
        n = count[0]
        ans += n * (n - 1) / 2
    if 30 in count:
        n = count[30]
        ans += n * (n - 1) / 2
    for k, v in count.items():
        if k < 30 and 60 - k in count:
            n = count[60 - k]
            ans += v * n
    return int(ans)
```