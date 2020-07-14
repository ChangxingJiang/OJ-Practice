from typing import List

from toolkit import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # 计算链表长度
        size = 0
        node = root
        while node:
            node = node.next
            size += 1

        # 计算各个子串的长度
        avg_num = size // k
        plus_num = size % k

        ans = []
        node = root
        for i in range(k):
            num = avg_num + (i < plus_num)
            if num > 0:
                for _ in range(num - 1):
                    node = node.next
                point = node.next
                node.next = None
                ans.append(root)
                root = node = point
            else:
                ans.append(None)

        return ans


if __name__ == "__main__":
    ans = Solution().splitListToParts(ListNode([1, 2, 3]), k=5)
    for i in ans:
        print(i)
    # [[1],[2],[3],[],[]]

    ans = Solution().splitListToParts(ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), k=3)
    for i in ans:
        print(i)
    # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
