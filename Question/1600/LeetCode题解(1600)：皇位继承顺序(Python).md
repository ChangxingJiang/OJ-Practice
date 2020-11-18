# LeetCode题解(1600)：设计皇位继承顺序计算类(Python)

题目：[原题链接](https://leetcode-cn.com/problems/throne-inheritance/)（中等）

标签：设计、树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 808ms (38%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class ThroneInheritance:
    class People:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.die = False

    def __init__(self, kingName: str):
        self.head = self.People(kingName)
        self.dic = {kingName: self.head}

    def birth(self, parentName: str, childName: str) -> None:
        people = self.People(childName)
        self.dic[parentName].children.append(people)
        self.dic[childName] = people

    def death(self, name: str) -> None:
        self.dic[name].die = True

    def getInheritanceOrder(self) -> List[str]:
        self.ans = []

        def dfs(node):
            if node:
                if not node.die:
                    self.ans.append(node.name)
                for child in node.children:
                    dfs(child)

        dfs(self.head)

        return self.ans
```