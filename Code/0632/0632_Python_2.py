from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 生成初始范围
        scopes = [(n, n) for n in nums[0]]

        # 不断更新范围
        for num in nums[1:]:
            i1, i2 = 0, 0
            new_scopes = []
            while i1 < len(scopes) and i2 < len(num):
                scope = scopes[i1]
                n = num[i2]
                if n < scope[0]:
                    if not new_scopes or new_scopes[-1][0] < n:
                        new_scopes.append((n, scope[1]))
                    i2 += 1
                elif scope[0] <= n <= scope[1]:
                    new_scopes.append(scope)
                    i1 += 1
                else:
                    if new_scopes and new_scopes[-1][1] == n:
                        new_scopes.pop()
                    new_scopes.append((scope[0], n))
                    i1 += 1
            scopes = new_scopes

        return list(min(scopes, key=lambda s: s[1] - s[0]))


if __name__ == "__main__":
    print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))  # [20,24]
    print(Solution().smallestRange([
        [
            95387,
            95790,
            97307,
            98168,
            99868,
            99995,
            99995,
            100000
        ],
        [
            -69454,
            -17042,
            8172,
            50983,
            63432,
            72854,
            73012,
            80848,
            83723,
            85916,
            91759,
            99779,
            99913,
            99944,
            99994,
            99999,
            99999
        ],
        [
            65641,
            95910,
            97995,
            98196,
            98969,
            99008,
            99591,
            99732,
            99735,
            99896,
            99952,
            99989,
            99999,
            100000
        ]]))
