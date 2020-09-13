from typing import List


class Solution:
    def __init__(self):
        self.ans = set()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def iterator(lst, total, idx=0):
            if idx >= len(candidates):
                return

            num = candidates[idx]

            # 处理分支加上当前元素后小于目标值的情况
            if total + num < target:
                # 添加当前元素到分支
                iterator(lst + [num], total + num, idx + 1)

                # 不添加当前元素到分支
                iterator(lst, total, idx + 1)

            elif total + num == target:
                lst.append(num)
                self.ans.add(tuple(lst))

        iterator([], 0)

        return [list(elem) for elem in self.ans]


if __name__ == "__main__":
    # [
    #   [1, 7],
    #   [1, 2, 5],
    #   [2, 6],
    #   [1, 1, 6]
    # ]
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

    # [
    #   [1,2,2],
    #   [5]
    # ]
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
