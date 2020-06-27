class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left_index = 1
        right_index = num
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            s = pow(mid_index, 2)
            if s < num:
                left_index = mid_index + 1
            elif s > num:
                right_index = mid_index - 1
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))  # True
    print(Solution().isPerfectSquare(14))  # False
    print(Solution().isPerfectSquare(1))  # True
