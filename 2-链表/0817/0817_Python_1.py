from typing import List

from toolkit import ListNode


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numComponents(ListNode([0, 1, 2, 3]), [0, 1, 3]))  # 2
    print(Solution().numComponents(ListNode([0, 1, 2, 3, 4]), [0, 3, 1, 4]))  # 2
