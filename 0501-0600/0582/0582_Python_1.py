from collections import deque
from typing import List


class Solution:
    class Node:
        def __init__(self, pid):
            self.pid = pid
            self.children = set()

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        nodes = {0: self.Node(0)}

        # 构造节点
        # O(N)
        for i in range(len(pid)):
            nodes[pid[i]] = self.Node(pid[i])

        # 构造树
        # O(N)
        for i in range(len(pid)):
            nodes[ppid[i]].children.add(nodes[pid[i]])

        # 查询进程子树
        ans = []
        node_list = deque([nodes[kill]])
        while node_list:
            node = node_list.popleft()
            ans.append(node.pid)
            for child in node.children:
                node_list.append(child)

        return ans


if __name__ == "__main__":
    # [5,10]
    print(Solution().killProcess(pid=[1, 3, 10, 5], ppid=[3, 0, 5, 3], kill=5))
