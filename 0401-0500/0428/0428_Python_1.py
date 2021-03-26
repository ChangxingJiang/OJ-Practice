from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


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


if __name__ == "__main__":
    sub21 = Node(4)
    sub1 = Node(2)
    sub2 = Node(3, [sub21])
    tree = Node(1, [sub1, sub2])

    codec = Codec()
    code = codec.serialize(tree)
    print(code)
    print(codec.deserialize(code))
    print()

    codec = Codec()
    code = codec.serialize(None)
    print(code)
    print(codec.deserialize(code))
