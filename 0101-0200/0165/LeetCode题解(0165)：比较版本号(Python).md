# LeetCode题解(0165)：比较版本号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/compare-version-numbers/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M+N)$   | $O(M+N)$   | 40ms (69.46%) |
| Ans 2 (Python) | $O(M+N)$   | $O(M+N)$   | 44ms (43.37%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号转换为数字列表
        version1 = [int(s) for s in version1.split(".")]
        version2 = [int(s) for s in version2.split(".")]

        # 移除版本号末尾多余的0
        while version1 and version1[-1] == 0:
            version1.pop()
        while version2 and version2[-1] == 0:
            version2.pop()

        # 比较版本号
        while version1 or version2:
            if not version1:
                return -1
            if not version2:
                return 1
            v1 = version1.pop(0)
            v2 = version2.pop(0)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
```

解法二：

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号转换为数字列表
        version1 = [int(s) for s in version1.split(".")]
        version2 = [int(s) for s in version2.split(".")]
        N1, N2 = len(version1), len(version2)

        # 比较版本号
        for i in range(max(N1, N2)):
            i1 = version1[i] if i < N1 else 0
            i2 = version2[i] if i < N2 else 0
            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
        return 0
```