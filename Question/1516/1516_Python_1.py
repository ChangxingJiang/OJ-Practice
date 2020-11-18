class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        # 处理p为根节点的情况
        if root == p:
            q_parent = self.dfs2(root, q)  # Q节点的父节点
            q_parent.children.remove(q)
            q.children.append(p)
            return q

        # 寻找p节点的父节点
        p_parent = self.dfs2(root, p)  # P节点的父节点

        # 处理q节点就是p的父节点的情况
        if p_parent == q:
            return root

        # 处理q子树存在于p子树中的情况
        elif self.dfs1(p, q):
            q_parent = self.dfs2(p, q)  # Q节点的父节点
            q_parent.children.remove(q)
            idx = p_parent.children.index(p)  # P节点的父节点中P节点的序数
            q.children.append(p)
            p_parent.children[idx] = q
            return root

        # 处理q子树不存在于p子树中的情况
        else:
            p_parent.children.remove(p)
            q.children.append(p)
            return root

    # 判断q节点是否存在于当前子树中
    def dfs1(self, node, q):
        if node == q:
            return True
        else:
            return any(self.dfs1(child, q) for child in node.children)

    # 寻找指定节点的父节点
    def dfs2(self, node, aim):
        if aim in node.children:
            return node
        else:
            for child in node.children:
                find = self.dfs2(child, aim)
                if find:
                    return find


if __name__ == "__main__":
    pass
