# LeetCode题解(1089)：复写列表中的零(Python)

题目：[原题链接](https://leetcode-cn.com/problems/duplicate-zeros/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 48ms (82.04%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (91.02%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（使用列表的插入方法）：

```python
def duplicateZeros(self, arr: List[int]) -> None:
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop(-1)
```

解法二（两次遍历）：

```python
def duplicateZeros(self, arr: List[int]) -> None:
    # 统计一共复制了多少个0
    count = 0
    idx1 = 0
    while idx1 + count < len(arr):
        if arr[idx1] == 0:
            count += 1
        idx1 += 1

    idx1 -= 1  # 将循环中多自增的减回来

    idx2 = len(arr) - 1

    # 处理最后一个数字是0的情况，例如：[1, 0, 2, 3, 0, 0, 5, 0]
    if count + idx1 + 1 > len(arr):
        arr[idx2] = arr[idx1]
        idx1 -= 1
        idx2 -= 1
        count -= 1

    # 移动结果
    while count:
        arr[idx2] = arr[idx1]
        if arr[idx1] == 0:
            idx2 -= 1
            arr[idx2] = arr[idx1]
            count -= 1
        idx1 -= 1
        idx2 -= 1
```