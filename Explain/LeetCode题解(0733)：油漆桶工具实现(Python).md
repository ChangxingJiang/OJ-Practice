# LeetCode题解(0733)：油漆桶工具实现(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flood-fill/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (96.92%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 88ms (91.46%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    h = len(image)
    w = len(image[0])
    aim_list = [(sr, sc)]
    old_color = image[sr][sc]
    while len(aim_list) > 0:
        (r, c) = aim_list.pop()
        image[r][c] = newColor
        if r > 0 and image[r - 1][c] == old_color:
            aim_list.append((r - 1, c))
        if c > 0 and image[r][c - 1] == old_color:
            aim_list.append((r, c - 1))
        if r < h - 1 and image[r + 1][c] == old_color:
            aim_list.append((r + 1, c))
        if c < w - 1 and image[r][c + 1] == old_color:
            aim_list.append((r, c + 1))
    return image
```

解法二：

```python
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    h = len(image)
    w = len(image[0])

    old_color = image[sr][sc]

    if old_color == newColor:
        return image

    def change(r, c):
        if image[r][c] == old_color:
            image[r][c] = newColor
            if r > 0:
                change(r - 1, c)
            if c > 0:
                change(r, c - 1)
            if r < h - 1:
                change(r + 1, c)
            if c < w - 1:
                change(r, c + 1)

    change(sr, sc)

    return image
```