# LeetCode题解(1042)：不邻接种花/地图染色(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flower-planting-with-no-adjacent/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(P+N)$   | $O(P)$     | 532ms (64.19%) |
| Ans 2 (Python) | $O(P+N)$   | $O(P)$     | 476ms (98.90%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟+哈希表）：

```python
def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
    hashmap = {}
    for path in paths:
        if path[0] not in hashmap:
            hashmap[path[0]] = [path[1]]
        else:
            hashmap[path[0]].append(path[1])
        if path[1] not in hashmap:
            hashmap[path[1]] = [path[0]]
        else:
            hashmap[path[1]].append(path[0])

    color = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        if i not in hashmap:
            color[i] = 1
        else:
            apt = [1, 2, 3, 4]
            for near in hashmap[i]:
                if color[near] != 0 and color[near] in apt:
                    apt.remove(color[near])
            color[i] = apt[0]

    return color[1:]
```

解法二（将哈希表改为数组）：

```python
def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
    hashmap = [[] for _ in range(N + 1)]
    for path in paths:
        if path[0] > path[1]:
            hashmap[path[0]].append(path[1])
        else:
            hashmap[path[1]].append(path[0])

    color = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        apt = [1, 2, 3, 4]
        for near in hashmap[i]:
            if color[near] != 0 and color[near] in apt:
                apt.remove(color[near])
        color[i] = apt[0]

    return color[1:]
```







