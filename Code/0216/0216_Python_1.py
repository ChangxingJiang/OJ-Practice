from typing import List


class Solution:
    def __init__(self):
        self.ans = set()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def iterator(lst, total, num=1):
            # 处理当分支已经达到3个的情况
            if len(lst) == k:
                if total == n:
                    self.ans.add(tuple(lst))

            # 处理分支加上当前元素后小于目标值的情况
            if num <= 9 and total + num <= n:
                # 添加当前元素到分支
                iterator(lst + [num], total + num, num + 1)

                # 不添加当前元素到分支
                iterator(lst, total, num + 1)

        iterator([], 0)

        return [list(elem) for elem in self.ans]


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))  # [[1,2,4]]
    print(Solution().combinationSum3(3, 9))  # [[1,2,6], [1,3,5], [2,3,4]]
    print(Solution().combinationSum3(3, 15))  # [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
