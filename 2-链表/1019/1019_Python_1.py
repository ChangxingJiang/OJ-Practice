from typing import List

from toolkit import ListNode


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().nextLargerNodes(ListNode([2, 1, 5])))  # [5,5,0]
    print(Solution().nextLargerNodes(ListNode([2, 7, 4, 3, 5])))  # [1,7,5,1,9,2,5,1]
    print(Solution().nextLargerNodes(ListNode([1, 7, 5, 1, 9, 2, 5, 1])))  # [7,9,9,9,0,5,0,0]
