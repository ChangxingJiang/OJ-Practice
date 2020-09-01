# LeetCode题解(1233)：删除为其他文件夹的子文件夹的文件夹(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/)（中等）

标签：字符串

| 解法           | 时间复杂度                     | 空间复杂度                     | 执行用时       |
| -------------- | ------------------------------ | ------------------------------ | -------------- |
| Ans 1 (Python) | $O(N×C)$ : 其中C为路径平均深度 | $O(N×C)$ : 其中C为路径平均深度 | 376ms (28.06%) |
| Ans 2 (Python) | $O(NlogN)$                     | $O(NlogN)$                     | 244ms (92.45%) |
| Ans 3 (Python) |                                |                                |                |

解法一（暴力解法）：

```python
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 将所有地址存入集合中
        folders = set(folder)

        # 遍历判断是否存在于集合中
        ans = []
        for f in folder:
            path = f.split("/")
            for i in range(1, len(path) - 1):
                if "/".join(path[:i + 1]) in folders:
                    break
            else:
                ans.append(f)

        return ans
```

解法二（排序法）：

```python
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        last = " "
        folder.sort()
        for f in folder:
            if not f.startswith(last):
                ans.append(f)
                last = f + "/"
        return ans
```