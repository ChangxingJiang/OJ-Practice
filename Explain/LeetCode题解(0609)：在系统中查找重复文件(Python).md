# LeetCode题解(0609)：在文件路径列表中查找重复内容的文件(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-duplicate-file-in-system/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (91.87%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            for file in path[1:]:
                file = file.split("(")
                content = file[1].replace(")", "")
                hashmap[content].append(folder + "/" + file[0])

        ans = []
        for key, value in hashmap.items():
            if len(value) >= 2:
                ans.append(value)

        return ans
```