# LeetCode题解(0428)：序列化和反序列化N叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/serialize-and-deserialize-n-ary-tree/)（困难）

标签：树、N叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 64ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（层序遍历）：

```python
class Codec:
    def serialize(self, root: 'Node') -> str:
        # 处理空树的特殊情况
        if not root:
            return ""

        count = 1  # 队列中有效节点个数
        queue = deque([root])
        ans = [root.val, "N"]
        while queue and count:
            p = queue.popleft()
            count -= 1
            if p:
                if p.children:
                    for c in p.children:
                        count += 1
                        queue.append(c)
                        ans.append(c.val)
            ans.append("N")
        while ans and ans[-1] == "N":
            ans.pop()
        return " ".join(str(n) for n in ans)

    def deserialize(self, data: str) -> 'Node':
        # 处理空树的特殊情况
        if not data:
            return None

        data = data.split(" ")

        root = Node(val=int(data[0]), children=[])
        queue = deque([root])
        now_node = None
        for i in range(1, len(data)):
            if data[i] == "N":
                now_node = queue.popleft()
            else:
                node = Node(val=int(data[i]), children=[])
                now_node.children.append(node)
                queue.append(node)
        return root
```