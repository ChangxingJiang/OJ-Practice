from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 下一个组合
        def change(group):
            for i in range(k):
                if group[k - 1 - i] < n - i:
                    group[k - 1 - i] += 1
                    for j in range(k - i, k):
                        group[j] = group[j - 1] + 1
                    return True
            return False

        ans = []
        now = [i for i in range(1, k + 1)]
        ans.append(now.copy())
        while change(now):
            ans.append(now.copy())

        return ans


if __name__ == "__main__":
    # [
    #   [2,4],
    #   [3,4],
    #   [2,3],
    #   [1,2],
    #   [1,3],
    #   [1,4],
    # ]
    print(Solution().combine(4, 2))

    # [[1]]
    print(Solution().combine(1, 1))
