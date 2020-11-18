class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 翻转180度后的对应表
        reverse_lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in reverse_lst or num[right] not in reverse_lst:
                return False
            if reverse_lst[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    print(Solution().isStrobogrammatic("69"))  # True
    print(Solution().isStrobogrammatic("88"))  # True
    print(Solution().isStrobogrammatic("962"))  # False
    print(Solution().isStrobogrammatic("1"))  # True
    print(Solution().isStrobogrammatic("25"))  # False
