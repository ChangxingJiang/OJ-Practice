# LeetCode题解(0914)：卡牌分组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (88.36%) |
| Ans 2 (Python) | --         | --         | 44ms (88.36%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表+公因数）：

```python
def hasGroupsSizeX(self, deck: List[int]) -> bool:
    hashmap = {}
    for d in deck:
        if d not in hashmap:
            hashmap[d] = 1
        else:
            hashmap[d] += 1

    nums = list(hashmap.values())
    i = 2
    while i <= min(nums):
        for n in nums:
            if n % i != 0:
                break
        else:
            return True
        i += 1
    return False
```

解法二（Pythonic）：

```python
def hasGroupsSizeX(self, deck: List[int]) -> bool:
    return functools.reduce(math.gcd, list(collections.Counter(deck).values())) >= 2
```