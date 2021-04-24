from typing import List


# 生成排列列表
def permute(idxs, nums, maximum):
    size = len(idxs)
    ans = []

    def dfs(i, add, now):
        """当前正在选择哪一个、当前已经选择多少、当前序列"""
        if add == maximum:
            ans.append(now)
        elif i == size:  # 选择完成但总量不够
            return
        else:
            for j in range(min(maximum - add, nums[i]) + 1):
                dfs(i + 1, add + j, now + [idxs[i]] * j)

    dfs(0, 0, [])

    # print(idxs, nums, "->", ans)

    return ans


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        if batchSize == 1:
            return len(groups)

        count = [0] * batchSize  # 每个余数的数量

        for group in groups:
            remainder = group % batchSize
            count[remainder] += 1

        # print("余数列表:", count)

        # 所有可以除尽的组最先安排，一定都是开心的
        ans = count[0]
        count[0] = 0

        print(ans, count)

        # 当前最多在4组内剩下30个元素
        # 四组每组选择拿0-9个，所有可能为10^4
        # 每次至少拿走2个，最多15*10^4

        # 当前剩余组的总数
        total_waiting = sum(count)

        # 当前尝试拼凑的余数数量
        # 从少到多逐个尝试
        now_trying = 2

        # 尝试用剩下的余数拼出尽可能多的batchSize
        while now_trying <= total_waiting:
            # 计算当前剩余的组及剩余的数量
            waiting_idx = [i for i in range(1, batchSize) if count[i] > 0]
            waiting_num = [count[i] for i in range(1, batchSize) if count[i] > 0]
            # print(waiting_idx)
            # print(waiting_num)
            for choose_lst in permute(waiting_idx, waiting_num, now_trying):
                # 如果组合可以除尽
                if sum(choose_lst) % batchSize == 0:
                    print("发现组:", choose_lst)
                    ans += 1
                    total_waiting -= now_trying
                    for i in choose_lst:
                        count[i] -= 1
                    break
            else:
                now_trying += 1

        # 如果还有剩下的组，那么其中的第一组一定是开心的
        if total_waiting > 0:
            # print("剩余组:", total_waiting)
            ans += 1

        print(ans, count)

        return ans


if __name__ == "__main__":
    print(Solution().maxHappyGroups(batchSize=3, groups=[1, 2, 3, 4, 5, 6]))  # 4
    print(Solution().maxHappyGroups(batchSize=4, groups=[1, 3, 2, 5, 2, 2, 1, 6]))  # 4
    print(Solution().maxHappyGroups(
        batchSize=8,
        groups=[8, 8, 4, 1, 6, 8, 6, 3, 7, 7, 2, 4, 1, 6, 7, 4, 1, 4, 2, 4, 4, 7, 6, 1, 5, 1, 3, 4, 1, 1]))  # 16

    # 自制测试用例
    # print(Solution().maxHappyGroups(batchSize=9, groups=[1, 5, 7]))  # 1
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 2, 3, 3, 3, 3, 3, 4, 5, 6]))  # 5
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 2, 3, 4, 5, 6, 1, 2, 1, 2]))  # 5
    # print(Solution().maxHappyGroups(batchSize=5, groups=[1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]))  # 3
