# LeetCode题解(1487)：修改文件名列表使文件名唯一(Python)

题目：[原题链接](https://leetcode-cn.com/problems/making-file-names-unique/)（中等）

标签：字符串、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 124ms (86.44%) |
| Ans 3 (Python) |            |            |                |

解法一（暴力集合解法）：

```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_set = set()
        ans = []
        for name in names:
            # 处理还没有重名的情况
            if name not in name_set:
                name_set.add(name)
                ans.append(name)

            # 处理出现重名的情况
            else:
                # 计算当前文件夹名的名称部分和计数部分
                word = name
                num = 1

                # 调整当前文件夹名的数量至没有重名
                while word + "(" + str(num) + ")" in name_set:
                    num += 1
                new_name = word + "(" + str(num) + ")"
                name_set.add(new_name)
                ans.append(new_name)
        return ans
```

解法二（哈希表记录）：

```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        count = {}
        ans = []
        for name in names:
            s = name
            while s in count:
                s = "".join([name, "(", str(count[name]), ")"])
                count[name] += 1
            count[s] = 1
            ans.append(s)
        return ans
```