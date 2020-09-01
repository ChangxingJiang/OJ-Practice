from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 使用二进制数记录每一个位置的前缀字母的奇偶情况
        lst = [0]
        for i, ch in enumerate(s):
            # (1 << (ord(ch) - 97)) 当前字母在二进制数中的位置
            # lst[i] ^ (1 << (ord(ch) - 97)) 如果当前字母为奇数(1)则改为(0)，反之则改为(1)
            lst.append(lst[i] ^ (1 << (ord(ch) - 97)))

        # 遍历计算每一个query是否为回文串
        ans = []
        for left, right, k in queries:
            # lst[left] 左侧位置前缀字母的奇偶情况
            # lst[right + 1] 右侧位置前缀字母的奇偶情况
            # lst[left] ^ lst[right + 1] 左右侧位置前缀字母奇偶情况差异
            differ = bin(lst[left] ^ lst[right + 1]).count("1")
            ans.append(differ // 2 <= k)
        return ans


if __name__ == "__main__":
    # [true,false,false,true,true]
    print(Solution().canMakePaliQueries(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))

    # [true,false,true,true,true,true,true,false,true,false,true,true,true]
    print(Solution().canMakePaliQueries(
        s="hunu",
        queries=[[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1],
                 [0, 3, 0], [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 1], [1, 1, 1]])
    )
