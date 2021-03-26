from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def iterator(lst, total, idx=0):
            num = candidates[idx]

            # 处理当前分支仍小于目标值的情况
            if total + num < target:
                # 进入添加当前值的分支
                iterator(lst + [num], total + num, idx)

                # 进入不添加当前值的分支
                if idx + 1 < len(candidates):
                    iterator(lst, total, idx + 1)

            # 处理当前分支等于目标值的情况
            elif total + num == target:
                lst.append(num)
                self.ans.append(lst.copy())

        iterator(lst=[], total=0)

        return self.ans


if __name__ == "__main__":
    # [
    #   [7],
    #   [2,2,3]
    # ]
    print(Solution().combinationSum([2, 3, 6, 7], 7))

    # [
    #   [2,2,2,2],
    #   [2,3,3],
    #   [3,5]
    # ]
    print(Solution().combinationSum([2, 3, 5], 8))
