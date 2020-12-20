# LeetCode题解(0533)：孤独像素II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lonely-pixel-ii/)（中等）

标签：数组、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 548ms (55.10%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        dic_row = collections.defaultdict(list)
        count_row = []
        for i in range(len(picture)):
            row = picture[i]
            count_row.append(row.count("B"))
            if count_row[-1] == N:
                dic_row[tuple(row)].append(i)

        rows = list(dic_row.values())
        row_dic = {}
        for r, lst in enumerate(rows):
            for i in lst:
                row_dic[i] = r

        # print(count_row)
        # print(row_dic)

        ans = 0

        for j in range(len(picture[0])):
            count = 0
            row_lst = []
            for i in range(len(picture)):
                if picture[i][j] == "B":
                    count += 1
                    row_lst.append(i)
            if count == N:
                row_set = set()
                fail = False
                for r in row_lst:
                    if r not in row_dic:
                        fail = True
                        break
                    row_set.add(row_dic[r])
                if not fail and len(row_set) == 1:
                    ans += count

        return ans
```