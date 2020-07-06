from typing import List

from toolkit import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        pass


if __name__ == "__main__":
    print(Solution().splitListToParts(ListNode([1, 2, 3]), k=5))
    # [[1],[2],[3],[],[]]

    print(Solution().splitListToParts(ListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), k=3))
    # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
