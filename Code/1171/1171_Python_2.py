from toolkit import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        while True:
            hashmap = {0: ans}
            sum_ = 0
            node = ans.next
            while node:
                sum_ += node.val
                if sum_ not in hashmap:
                    hashmap[sum_] = node
                else:
                    hashmap[sum_].next = node.next
                    break
                node = node.next
            else:
                break

        return ans.next


if __name__ == "__main__":
    print(Solution().removeZeroSumSublists(ListNode([1, 2, -3, 3, 1])))  # [3,1]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, 4])))  # [1,2,4]
    print(Solution().removeZeroSumSublists(ListNode([1, 2, 3, -3, -2])))  # [1]
    print(Solution().removeZeroSumSublists(ListNode([1, 3, 2, -3, -2, 5, 5, -5, 1])))  # [1,5,1]
