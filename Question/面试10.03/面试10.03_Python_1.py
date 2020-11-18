from typing import List


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        size = len(arr)

        # 二分查找旋转位置
        aim = arr[0]
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > aim:
                left = mid + 1
            elif arr[mid] < aim:
                right = mid

            # 处理重复值的问题
            elif right - 1 > 0 and arr[right - 2] > arr[right - 1]:
                left = right - 1
                break
            else:
                right -= 1
        move = left

        # print("偏移量:", move)

        # 二分查找目标值
        ans = -1
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2
            actual_mid = (mid + move) % size
            # print(left, right, "->", mid, "->", actual, "=", arr[actual])
            if arr[actual_mid] < target:
                left = mid + 1
            elif arr[actual_mid] > target:
                right = mid

            # 处理最终结果是针对实际坐标
            else:
                if ans == -1 or ans > actual_mid:
                    ans = actual_mid
                actual_right = (right + move) % size
                if arr[actual_right] == target:
                    if actual_right < actual_mid:
                        return 0
                    else:
                        right = mid
                else:
                    right -= 1

        return ans


if __name__ == "__main__":
    # 8
    print(Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=5))

    # -1
    print(Solution().search(arr=[15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target=11))

    # 5
    print(Solution().search(arr=[1, 1, 1, 1, 1, 2, 1, 1, 1], target=2))

    # 0
    print(Solution().search(arr=[5, 5, 5, 1, 2, 3, 4, 5], target=5))
