from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 生成2的倍数数列
        num_lst = [1]
        while num_lst[-1] <= label:
            num_lst.append(num_lst[-1] * 2)

        # 计算当前点的真实坐标
        if len(num_lst) % 2 == 1:
            now_idx = num_lst[-2] + num_lst[-1] - label - 1
        else:
            now_idx = label

        # 生成坐标列表
        idx_lst = []
        while now_idx > 1:
            idx_lst.append(now_idx)
            now_idx //= 2
        idx_lst.append(1)
        idx_lst.reverse()

        # print(num_lst, idx_lst)

        ans = []
        reverse = False
        for i in range(len(idx_lst)):
            idx = idx_lst[i]
            num1 = num_lst[i]
            num2 = num_lst[i + 1]
            if reverse:
                ans.append(num1 + num2 - idx - 1)
            else:
                ans.append(idx)
            reverse = not reverse

        return ans


if __name__ == "__main__":
    # [1,3,4,14]
    print(Solution().pathInZigZagTree(14))

    # [1,2,6,10,26]
    print(Solution().pathInZigZagTree(26))

    # [1,3,4,15,16]
    print(Solution().pathInZigZagTree(16))
