from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # 处理特殊情况
        if len(A) == 2:
            return A

        # 滑动窗口计算数量
        def count(guess):
            total = 0
            l = 0
            m_v, m_g = 1, []  # 存储略小于查询值的那一个分数
            for r in range(len(A)):
                while l < r:
                    v = A[l] / A[r]
                    # if guess <= v < m_v:
                    #     m_v, m_g = v, [A[l], A[r]]
                    if v >= guess:
                        if v < m_v:
                            m_v, m_g = v, [A[l], A[r]]
                        break
                    l += 1
                # print(l, r, A[l], A[r])
                total += r - l

            # 如果所有值都比目标值大，则选取最接近目标值的数
            if m_v == 0:
                m_g = [A[0], A[-1]]

            return total, m_g

        size = len(A)

        # 计算第K小的数时第几大的数
        T = size * (size - 1) // 2 - K + 1

        left, right = 0, 1
        for i in range(1000):  # 最多二分查找1000次
            mid = (left + right) / 2
            res, min_group = count(mid)
            # print(left, right, "->", mid, "=", res)
            if res > T:  # 如果比mid大的数多于目标值，说明mid小了
                left = mid
            elif res < T:  # 如果比mid大的数少于目标值，说明mid大了
                right = mid
            else:
                return min_group


if __name__ == "__main__":
    # [2,5]
    print(Solution().kthSmallestPrimeFraction(A=[1, 2, 3, 5], K=3))

    # [1,79]
    print(Solution().kthSmallestPrimeFraction(A=[1, 79], K=1))

    # [1,47]
    print(Solution().kthSmallestPrimeFraction(A=[1, 29, 47], K=1))
