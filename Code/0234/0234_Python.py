from toolkit import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().isPalindrome(ListNode([1, 2])))  # False
    print(Solution().isPalindrome(ListNode([1, 2, 2, 1])))  # True
    print(Solution().isPalindrome(ListNode([1])))  # True
    print(Solution().isPalindrome(ListNode([1, 2, 1])))  # True
