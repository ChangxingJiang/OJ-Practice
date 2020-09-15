import math
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label > 1:
            print(label)
            ans.append(label)
            last_line_num = int(math.log2(label))  # 上一行的行数
            last_line_right = pow(2, last_line_num - 1)  # 当前行最左侧的数在未Z字型转换的完全二叉树中的坐标
            label = 3 * last_line_right - label // 2 - 1

        ans.append(1)
        return ans[::-1]


if __name__ == "__main__":
    # [1,3,4,14]
    print(Solution().pathInZigZagTree(14))

    # [1,2,6,10,26]
    print(Solution().pathInZigZagTree(26))

    # [1,3,4,15,16]
    print(Solution().pathInZigZagTree(16))
