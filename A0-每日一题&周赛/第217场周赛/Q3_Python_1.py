from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        size = len(nums)

        # 树状数组及相关函数
        tree = [0] * (limit * 2 + 1)

        def add(k, x):
            while k <= limit * 2:
                tree[k] += x
                k += k & (-k)

        def range_add(l, r, x):
            add(l, x)
            add(r + 1, -x)

        def query(k: int) -> int:
            ans = 0
            while k > 0:
                ans += tree[k]
                k -= k & (-k)
            return ans

        min_val, max_val = 2, 200001  # 可以生成的最小值

        for i in range(size // 2):
            j = (size - 1) - i

            v1, v2 = nums[i], nums[j]

            # 2次操作可以得到的最大值
            val5 = (v1 if v1 > limit else limit) + (v2 if v2 > limit else limit)
            # 1次操作可以得到的最大值
            if v1 > limit and v2 > limit:
                val4 = v1 + v2
            elif v1 > limit >= v2:
                val4 = v1 + limit
            elif v1 <= limit < v2:
                val4 = limit + v2
            else:  # v1 < limit and v2 < limit
                val4 = max(v1, v2) + limit
            # 0次操作可以得到的值
            val3 = v1 + v2
            # 1次操作可以得到的最小值
            if v1 > limit and v2 > limit:
                val2 = v1 + v2
            elif v1 > limit >= v2:
                val2 = v1 + 1
            elif v1 <= limit < v2:
                val2 = 1 + v2
            else:  # v1 < limit and v2 < limit
                val2 = min(v1, v2) + 1
            # 2次操作可以得到的最小值
            val1 = (v1 if v1 > limit else 1) + (v2 if v2 > limit else 1)

            # 更新最大值、最小值
            min_val = max(min_val, val1)
            max_val = min(max_val, val5)

            # 更新树状数组
            range_add(val1, val2 - 1, 2)
            range_add(val2, val3 - 1, 1)
            range_add(val3 + 1, val4, 1)
            range_add(val4 + 1, val5, 2)

            # print(v1, v2, "->", val1, val2, val3, val4, val5, "(", min_val, max_val, ")", "->",
            #       [query(i) for i in range(limit * 2 + 1)])

        # 计算最终结果
        ans = 200001
        for i in range(min_val, min(limit * 2, max_val) + 1):
            ans = min(ans, query(i))
            # print(i, ":", query(i))
        return ans


if __name__ == "__main__":
    print(Solution().minMoves(nums=[1, 2, 4, 3], limit=4))  # 1
    print(Solution().minMoves(nums=[1, 2, 2, 1], limit=2))  # 2
    print(Solution().minMoves(nums=[1, 2, 1, 2], limit=2))  # 0

    print(Solution().minMoves(nums=[1, 2, 5, 3], limit=4))  # 1
    print(Solution().minMoves(nums=[1, 2, 5, 7], limit=4))  # 1

    print(Solution().minMoves(nums=[1, 3, 1, 1, 1, 2, 3, 2, 3, 1, 3, 2, 1, 3], limit=3))  # 4
