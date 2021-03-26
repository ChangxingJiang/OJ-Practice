class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while fast != 1 and slow != 1:
            fast = sum([int(x) * int(x) for x in str(fast)])
            fast = sum([int(x) * int(x) for x in str(fast)])
            slow = sum([int(x) * int(x) for x in str(slow)])
            if fast == slow and fast != 1:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isHappy(19))  # True
    print(Solution().isHappy(10))  # True
