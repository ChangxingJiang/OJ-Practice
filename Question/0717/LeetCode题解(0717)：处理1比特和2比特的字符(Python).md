# LeetCode题解(0717)：处理1比特和2比特的字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 68ms (56.53%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 64ms (74.93%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正向遍历）：

```python
def isOneBitCharacter(self, bits: List[int]) -> bool:
    t = False
    for i in range(len(bits) - 1):
        if t:
            t = False
        else:
            if bits[i] == 1:
                t = True
    return not t
```

解法二（反向遍历）：

```python
def isOneBitCharacter(self, bits: List[int]) -> bool:
    n = 0
    for b in bits[-2::-1]:
        if b == 0:
            break
        else:
            n += 1
    return n % 2 == 0
```