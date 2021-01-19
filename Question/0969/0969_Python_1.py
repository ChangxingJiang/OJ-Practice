from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        now_idx = len(arr) - 1

        while now_idx > 0:
            # 寻找最大值
            max_val = max(arr)

            # 最大值已经在数组末尾
            if arr[now_idx] == max_val:
                arr.pop()
                now_idx -= 1

            # 最大值还不在数组末尾
            else:
                # 将最大值移动到末尾
                max_idx = arr.index(max_val)
                ans.append(max_idx + 1)
                ans.append(now_idx + 1)

                # 更新数组和数组末尾
                arr = arr[max_idx + 1:][::-1] + arr[:max_idx]
                now_idx -= 1

        return ans


if __name__ == "__main__":
    print(Solution().pancakeSort([3, 2, 4, 1]))  # [4,2,4,3]
    print(Solution().pancakeSort([1, 2, 3]))  # []
    print(Solution().pancakeSort([1, 4, 2, 3]))  # [2, 4, 1, 3]
