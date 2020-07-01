# LeetCode题解(0788)：旋转数字后有效的数字数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotated-digits/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 108ms (57.60%) |
| Ans 2 (Python) | $O(NlogN)$ | $O(logN)$  | 104ms (62.36%) |
| Ans 3 (Python) | $O(1)$     | $O(1)$     | 32ms (100.00%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力算法）：

```python
def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N + 1):
        s = str(i)
        n = ""
        for c in s:
            if c in ["0", "1", "8"]:
                n += c
            elif c == "5":
                n += "2"
            elif c == "2":
                n += "5"
            elif c == "6":
                n += "9"
            elif c == "9":
                n += "6"
            else:
                break
        else:
            if int(n) != i:
                ans += 1
    return ans
```

解法二（更好的暴力方法）：

```python
def rotatedDigits(self, N: int) -> int:
    ans = 0
    for i in range(1, N + 1):
        s = str(i)
        differ = False
        for c in s:
            if c in ["2", "5", "6", "9"]:
                differ = True
            elif c in ["3", "4", "7"]:
                break
        else:
            if differ:
                ans += 1
    return ans
```

解法三（进制转换）：

![LeetCode题解(0788)：截图1.png](LeetCode题解(0788)：截图1.png)

> **【思路】**
>
> 0、1、2、5、6、8、9分别对应七进制的0、1、2、3、4、5、6；0、1、8分别对应三进制的0、1、2。
>
> 例如：
>
> 10 —— 七进制10转换为10，三进制10转换为3；结果：7 - 3 = 4
>
> 12 ——七进制12转换为9，三进制11转换为4；结果：9 - 4 = 5
>
> 细节：如果在某一位上出现了不存在于以上对应中的数，则该位向下取，其后的位取最大值。例如，130在转换为三进制时，十位的3不存在于对应表中，则十位取1对应的结果，个位取三进制的最大值2，即118。
>
> 具体实现如下：

```python
def rotatedDigits(self, N: int) -> int:
    d7 = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "2",
        "4": "2",
        "5": "3",
        "6": "4",
        "7": "4",
        "8": "5",
        "9": "6"
    }
    o7 = {"3", "4", "7"}
    d3 = {
        "0": "0",
        "1": "1",
        "2": "1",
        "3": "1",
        "4": "1",
        "5": "1",
        "6": "1",
        "7": "1",
        "8": "2",
        "9": "2"
    }
    o3 = {"2", "3", "4", "5", "6", "7", "9"}

    S = str(N)
    S7 = S3 = ""
    off = False
    for s in S:
        if off:
            S3 += "2"
        else:
            off = s in o3
            S3 += d3[s]

    off = False
    for s in S:
        if off:
            S7 += "6"
        else:
            off = s in o7
            S7 += d7[s]

    return int(S7, base=7) - int(S3, base=3)
```