# LeetCode题解(0913)：猫和老鼠(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cat-and-mouse/)（困难）

标签：极小化极大、动态规划、广度优先搜索、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^3)$   | 416ms (74.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def count(t, x, y):
            """
            :param t: 当前移动时间
            :param x: 当前老鼠的位置
            :param y: 当前猫的位置
            :return: 当前的游戏情况
            """
            # 处理猫抓到老鼠的情况
            if x == y:
                return 2

            # 处理老鼠进洞的情况
            if x == 0:
                return 1

            # 处理连续出现重复位置的情况
            if t == 2 * size:
                return 0

            # 处理老鼠移动的情况
            if t % 2 == 0:
                cat_can_win = True
                for i in graph[x]:
                    res = count(t + 1, i, y)
                    if res == 1:  # 处理老鼠能进洞的情况
                        return 1
                    elif res == 0:
                        cat_can_win = False
                if cat_can_win:
                    return 2
                else:
                    return 0

            # 处理猫移动的情况
            else:
                mouse_can_win = True
                for i in graph[y]:
                    if i == 0:  # 忽略老猫进洞的情况
                        continue
                    res = count(t + 1, x, i)
                    if res == 2:
                        return 2
                    elif res == 0:
                        mouse_can_win = False
                if mouse_can_win:
                    return 1
                else:
                    return 0

        size = len(graph)
        return count(0, 1, 2)
```