import collections
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        size = len(nums)

        count = collections.Counter(nums)

        # 处理无法分配的情况
        if count.most_common(1)[0][1] > k:
            return -1

        nums.sort()

        print("初始数组:", nums)

        # 处理k为1的情况
        if k == 1:
            return nums[-1] - nums[0]

        # 计算每个子集的元素数
        s = size // k

        # 生成每一段的计数器
        part_count = []
        for i in range(0, len(nums), s):
            part_count.append(collections.Counter(nums[i:i + s]))

        finish = False
        while not finish:
            finish = True
            for i in range(0, len(nums), s):
                p1 = i // s
                # 当前分段
                p1_min = nums[i]
                part_max = nums[i + s - 1]

                # 寻找重复值
                while True:
                    has_same = False
                    for ch1, v in list(part_count[p1].items()):
                        if v > 1:
                            finish = False
                            has_same = True
                            # 寻找重复值元素的坐标
                            for m in range(s):
                                if nums[i + m] == ch1:
                                    ii = i + m
                                    break
                            else:
                                # 理论上不可能出现的情况
                                return -2

                            # 向前寻找重复值的替换项
                            j1 = -1
                            j = i - 1
                            while j >= 0:
                                p2 = j // s
                                if nums[j] != ch1 and part_count[p2][ch1] == 0 and part_count[p1][nums[j]] == 0:
                                    j1 = j
                                    break
                                j -= 1

                            # 向后寻找重复值的替换项
                            j2 = -1
                            j = i + s
                            while j < size:
                                p2 = j // s
                                if nums[j] != ch1 and part_count[p2][ch1] == 0 and part_count[p1][nums[j]] == 0:
                                    j2 = j
                                    break
                                j += 1

                            if j1 != -1 and j2 != -1:
                                if part_count[j1 // s][nums[j1]] > 1:
                                    jj = j1
                                elif part_count[j2 // s][nums[j2]] > 1:
                                    jj = j2
                                elif p1_min - nums[j1] < nums[j2] - part_max:
                                    jj = j1
                                else:
                                    jj = j2
                            elif j1 == -1:
                                jj = j2
                            elif j2 == -1:
                                jj = j1

                            # print(nums[i:i + s], "替换:", ii, "->", (j1, j2), "->", jj)

                            p2 = jj // s
                            part_count[p1][nums[ii]] -= 1
                            part_count[p1][nums[jj]] += 1
                            part_count[p2][nums[jj]] -= 1
                            part_count[p2][nums[ii]] += 1

                            nums[ii], nums[jj] = nums[jj], nums[ii]

                            nums[p1 * s: p1 * s + s] = list(sorted(nums[p1 * s:p1 * s + s]))
                            nums[p2 * s: p2 * s + s] = list(sorted(nums[p2 * s:p2 * s + s]))

                            break

                    if not has_same:
                        break

        # 寻找可以交换情况
        for i in range(0, len(nums), s):
            p1 = i // s
            # 当前分段
            p1_min = nums[i]
            p1_max = nums[i + s - 1]

            for j1 in range(i, i + s):
                # 向后寻找交换项
                for j2 in range(i + s, size):
                    p2 = j2 // s
                    p2_min = nums[p2 * s]
                    p2_max = nums[p2 * s + s - 1]
                    if part_count[p2][nums[j1]] == 0 and part_count[p1][nums[j2]] == 0:
                        if nums[j1] > p2_min:
                            if max((nums[j1] - p2_min), 0) - max((nums[j2] - p1_max), 0) > 0:
                                part_count[p1][nums[j1]] -= 1
                                part_count[p1][nums[j2]] += 1
                                part_count[p2][nums[j2]] -= 1
                                part_count[p2][nums[j1]] += 1

                        nums[j1], nums[j2] = nums[j2], nums[j1]

                        nums[p1 * s: p1 * s + s] = list(sorted(nums[p1 * s:p1 * s + s]))
                        nums[p2 * s: p2 * s + s] = list(sorted(nums[p2 * s:p2 * s + s]))

                        break

        print("最终数组:", nums)

        ans = 0
        for i in range(0, len(nums), s):
            ans += nums[i + s - 1] - nums[i]
        return ans


if __name__ == "__main__":
    print("最终结果:", Solution().minimumIncompatibility(nums=[1, 2, 1, 4], k=2))  # 4
    print("最终结果:", Solution().minimumIncompatibility(nums=[6, 3, 8, 1, 3, 1, 2, 2], k=4))  # 6
    print("最终结果:", Solution().minimumIncompatibility(nums=[5, 3, 3, 6, 3, 3], k=3))  # -1
    print("最终结果:", Solution().minimumIncompatibility(nums=[3, 2, 1, 12, 10, 11, 6, 7, 6, 5, 10, 5], k=3))  # 15
    print("最终结果:", Solution().minimumIncompatibility(nums=[12, 8, 6, 6, 12, 1, 7, 9, 8, 9, 1, 9], k=4))  # 22

    print("最终结果:", Solution().minimumIncompatibility(nums=[1, 2, 3, 4], k=1))  # 3
