from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # 统计一共复制了多少个0
        count = 0
        idx1 = 0
        while idx1 + count < len(arr):
            if arr[idx1] == 0:
                count += 1
            idx1 += 1

        idx1 -= 1  # 将循环中多自增的减回来

        idx2 = len(arr) - 1

        # 处理最后一个数字是0的情况，例如：[1, 0, 2, 3, 0, 0, 5, 0]
        if count + idx1 + 1 > len(arr):
            arr[idx2] = arr[idx1]
            idx1 -= 1
            idx2 -= 1
            count -= 1

        # 移动结果
        while count:
            arr[idx2] = arr[idx1]
            if arr[idx1] == 0:
                idx2 -= 1
                arr[idx2] = arr[idx1]
                count -= 1
            idx1 -= 1
            idx2 -= 1


if __name__ == "__main__":
    param = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(param)
    print(param)  # [1,0,0,2,3,0,0,4]

    param = [1, 0, 2, 3, 0, 0, 5, 0]
    Solution().duplicateZeros(param)
    print(param)  # [1,0,0,2,3,0,0,0]

    param = [1, 2, 3]
    Solution().duplicateZeros(param)
    print(param)  # [1,2,3]
