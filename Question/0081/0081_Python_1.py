from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)

        # 二分查找旋转位置
        aim = nums[0]
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            # print(left, right, "->", mid, [nums[mid]])
            if nums[mid] > aim:
                aim = nums[mid]
                left = mid + 1
            elif nums[mid] < aim:
                right = mid

            # 处理重复值的问题
            else:  # nums[mid] == mid
                if left + 1 < size and nums[left] <= nums[left + 1]:
                    left += 1
                elif left == size - 1:
                    left = 0
                    break
                else:
                    left += 1
                    break

        move = left

        # print("偏移量:", move)

        # 二分查找目标值
        ans = -1
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            actual_mid = (mid + move) % size
            # print(left, right, "->", mid, "->", actual, "=", arr[actual])
            if nums[actual_mid] < target:
                left = mid + 1
            elif nums[actual_mid] > target:
                right = mid

            # 处理最终结果是针对实际坐标
            else:
                if ans == -1 or ans > actual_mid:
                    ans = actual_mid
                actual_right = (right + move) % size
                if nums[actual_right] == target:
                    if actual_right < actual_mid:
                        return True
                    else:
                        right = mid
                else:
                    right -= 1

        return ans != -1


if __name__ == "__main__":
    print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))  # True
    print(Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3))  # False
    print(Solution().search(nums=[1, 0, 1, 1, 1], target=0))  # True
    print(Solution().search(nums=[3, 1], target=3))  # True
    print(Solution().search(nums=[1, 1, 1, 1, 3], target=3))  # True
    print(Solution().search(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], target=2))  # True
