from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 生成2的倍数数列
        lst = [1]
        while lst[-1] <= label:
            lst.append(lst[-1] * 2)

        # 计算当前点的真实坐标
        if len(lst) % 2 == 1:
            idx = lst[-2] + lst[-1] - label - 1
            reverse = True
            most_val = lst[-1]
        else:
            idx = label
            reverse = False
            most_val = lst[-1]

        # 生成结果路径
        ans = []
        while idx > 1:
            most_val //= 2
            if reverse:
                ans.append(3 * most_val - idx - 1)
            else:
                ans.append(idx)
            idx //= 2
            reverse = not reverse
        ans.append(1)

        return list(reversed(ans))


if __name__ == "__main__":
    # [1,3,4,14]
    print(Solution().pathInZigZagTree(14))

    # [1,2,6,10,26]
    print(Solution().pathInZigZagTree(26))

    # [1,3,4,15,16]
    print(Solution().pathInZigZagTree(16))
