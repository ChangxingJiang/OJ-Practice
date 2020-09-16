from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 生成状态列表
        dp = [tuple()] * (target + 1)
        dp[0] = (0,)

        # 生成成本和最大数字的对应表
        cost_dict = {}
        for i, ch in enumerate(reversed(cost)):
            if ch not in cost_dict:
                cost_dict[ch] = 9 - i

        # 计算状态列表
        for i in range(1, target + 1):
            maybe_lst = []
            for c in cost_dict:
                idx = i - c
                if idx >= 0 and dp[idx]:
                    maybe_lst.append(dp[idx] + (cost_dict[c],))
            if maybe_lst:
                dp[i] = max(maybe_lst, key=lambda x: (len(x), x))

        # 返回结果
        return "".join([str(elem) for elem in dp[-1][1:]]) if dp[-1] else "0"


if __name__ == "__main__":
    print(Solution().largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))  # "7772"
    print(Solution().largestNumber(cost=[7, 6, 5, 5, 5, 6, 8, 7, 8], target=12))  # "85"
    print(Solution().largestNumber(cost=[2, 4, 6, 2, 4, 6, 4, 4, 4], target=5))  # "0"
    print(Solution().largestNumber(cost=[6, 10, 15, 40, 40, 40, 40, 40, 40], target=47))  # "32211"
    print(Solution().largestNumber(cost=[5, 4, 4, 5, 5, 5, 5, 5, 5], target=19))  # "9993"
    print(Solution().largestNumber(cost=[5, 6, 7, 3, 4, 6, 7, 4, 8], target=29))  # "884444444"
    print(Solution().largestNumber(cost=[3, 6, 8, 9, 3, 3, 3, 3, 3], target=20))  # "99993"
