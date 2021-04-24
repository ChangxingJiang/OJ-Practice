import collections
import copy
from typing import List


class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        # 依据单词长度分组
        # 时间:O(W) 其中W为单词总数(W<=1000)
        word_lst = collections.defaultdict(list)  # 依据单词长度分组
        for word in words:
            word_lst[len(word)].append(word)

        # 生成单词长度列表
        # 时间:O(L) 其中L为单词的不同长度数量(L<=100,L<=W)
        len_lst = list(sorted(word_lst.keys()))
        len_size = len(len_lst)

        # 初始化答案矩阵、答案矩阵的面积
        ans_lst, ans_val = [], 0

        # 遍历所有可能的单词长度组合
        # 循环次数(两层循环累计):O(L^2)
        for i1 in range(len_size - 1, -1, -1):
            # 计算矩阵的短边边长：l1为短边
            l1 = len_lst[i1]

            # 计算短边中每个位置的出现的字母集合
            # 每次执行:O(w) 其中w为长度为l1的单词数量(w<=W<=1000)
            # 累计执行:O(W)
            ch_set = collections.defaultdict(set)  # 每个长度的单词的开头字母列表
            for word in word_lst[l1]:
                for i, ch in enumerate(word):
                    ch_set[i].add(ch)

            for i2 in range(len_size - 1, i1 - 1, -1):
                # 计算矩阵的长边边长：l2为长边（l1可以与l2相等）
                l2 = len_lst[i2]

                # 如果矩阵面积小于已经得到的答案，则直接跳过当前情况
                if l1 * l2 <= ans_val:
                    continue

                # 遍历寻找所有可能的长边中的每一行
                # 每次执行:O(w1×l1) 其中w1为长度为l2的单词数量(w<=W<=1000)，l1为单词的字母数量(l1<=100)
                maybe_lst = [[] for _ in range(l1)]
                for word in word_lst[l2]:
                    for i in range(l1):
                        if set(word) <= ch_set[i]:
                            maybe_lst[i].append(word)

                # 如果存在任何一行没有被匹配成功则跳过当前情况
                if min(len(maybe_words) for maybe_words in maybe_lst) == 0:
                    continue

                # print(l1, l2, ":", maybe_lst)

                # 回溯计算所有可能的结果
                # 理论最坏情况的递归函数执行次数:O(w1^l1) —— 即每个值在每一行都有可行（但此时需要大量的长度为l1的单词支持，w1应该会比最大值小很多）
                def track(now, col_lst, res):
                    """ 回溯函数

                    :param now: 下一个需要选择的行序号
                    :param col_lst: 当前已经确定的列
                    :param res: 已经完成匹配的部分
                    """
                    # print("[回溯]", now, res, col_lst)
                    # 处理回溯完成的情况
                    if now == l1:
                        return [res]

                    # 遍历当前行序号的所有选择
                    # 循环累计执行:O(w2*l2) 当前行的所有可能选择
                    maybe_res = []
                    for maybe in maybe_lst[now]:
                        # 复制每列的选择列表
                        # O(w1)
                        col_lst_copy = [copy.copy(col) for col in col_lst]

                        # 检查当前选择是否符合要求
                        # 循环执行次数:O(l2)
                        fail = False
                        for j in range(l2):
                            # 移除当前列不符合要求的值
                            # 累计执行:O(w1)
                            for maybe_word in list(col_lst_copy[j]):
                                if maybe_word[now] != maybe[j]:
                                    col_lst_copy[j]._remove(maybe_word)

                            # 如果当前列剩余的选择数为0则剪枝
                            if len(col_lst_copy[j]) == 0:
                                fail = True
                                break

                        # 如果不符合要求则跳过当前选择
                        if fail:
                            continue

                        # 处理符合要求的循环
                        # O(w1)
                        maybe_res.extend(track(now + 1, col_lst_copy, res + [maybe]))

                    return maybe_res

                results = track(0, [set(word_lst[l1]) for _ in range(l2)], [])

                # print(results)

                if results:
                    ans_lst, ans_val = results[0], l1 * l2

        return ans_lst


if __name__ == "__main__":
    # [
    #    "this",
    #    "real",
    #    "hard"
    # ]
    print("最终结果:", Solution().maxRectangle(["this", "real", "hard", "trh", "hea", "iar", "sld"]))

    # ["eat",
    #  "ate",
    #  "tea"]
    print("最终结果:", Solution().maxRectangle(["eat", "tea", "tan", "ate", "nat", "bat"]))

    # ["aa","aa"]
    print("最终结果:", Solution().maxRectangle(["aa"]))
