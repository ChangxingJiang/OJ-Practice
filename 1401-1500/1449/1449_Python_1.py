from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 排序的所有成本选择
        ordered_cost = list(sorted(set(cost)))
        N = len(ordered_cost)

        # 回溯算法计算最多位数的选择
        length = target // ordered_cost[0]  # 最大可能位数
        lst = [0] * length  # 当前成本列表
        now = ordered_cost[0] * length  # 当前总成本
        maybe_lst = []
        while True:
            # 如果等于目标结果，则提取目标结果
            if now == target:
                maybe_lst.append(tuple(lst))

            # 处理已经完成回溯的情况
            if not lst:
                break

            # 继续完成回溯算法
            this_idx = lst.pop()  # 当前被替换对象
            next_idx = this_idx + 1
            now -= ordered_cost[this_idx]
            # 如果当前最后一位可以被替换为更大的且不超过target，则替换最后一位
            if next_idx < N and now + ordered_cost[next_idx] <= target:
                num = (target - now) // ordered_cost[next_idx]
                lst += [next_idx] * num
                now += ordered_cost[next_idx] * num

            # 如果当前最后一位不能被替换为更大的且不超过target，则替换前一位
            elif lst:
                this_idx = lst.pop()  # 当前被替换对象
                now -= ordered_cost[this_idx]
                next_idx = this_idx + 1
                if next_idx < N and now + ordered_cost[next_idx] <= target:
                    num = (target - now) // ordered_cost[next_idx]
                    lst += [next_idx] * num
                    now += ordered_cost[next_idx] * num

            # 如果已回溯到开头
            else:
                break

        # 如果没有回溯到结果则返回"0"
        if not maybe_lst:
            return "0"

        # 生成成本和最大数字的对应表
        cost_dict = {}
        for i, ch in enumerate(reversed(cost)):
            if ch not in cost_dict:
                cost_dict[ch] = 9 - i

        # 生成所有可能的结果
        ans = []
        for elem in maybe_lst:
            maybe_ans = [cost_dict[ordered_cost[elem]] for elem in elem]
            maybe_ans = int("".join([str(elem) for elem in sorted(maybe_ans, reverse=True)]))
            ans.append(maybe_ans)

        return str(max(ans))


if __name__ == "__main__":
    print(Solution().largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))  # "7772"
    print(Solution().largestNumber(cost=[7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))  # "85"
    print(Solution().largestNumber(cost=[2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))  # "0"
    print(Solution().largestNumber(cost=[6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))  # "32211"
    print(Solution().largestNumber(cost=[5, 4, 4, 5, 5, 5, 5, 5, 5], target=19))  # "9993"
    print(Solution().largestNumber(cost=[5, 6, 7, 3, 4, 6, 7, 4, 8], target=29))  # "884444444"
    print(Solution().largestNumber(cost=[3,6,8,9,3,3,3,3,3], target=20))  # "99993"
