class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        # 将字符串转换为以特殊序列分组的列表
        lst = []  # 主序列列表：不能拆分为子序列的部分+子序列位置标记
        sub_lst = []  # 子序列列表：特殊二进制子序列
        one_num = 0
        zero_num = 0
        for ch in S:
            if ch == "1":
                if zero_num:
                    if zero_num < one_num:
                        lst.append("1" * (one_num - zero_num))
                        lst.append("Sub")
                        sub_lst.append("1" * zero_num + "0" * zero_num)
                    elif zero_num == one_num:
                        lst.append("Sub")
                        sub_lst.append("1" * zero_num + "0" * zero_num)
                    else:
                        lst.append("Sub")
                        sub_lst.append("1" * one_num + "0" * one_num)
                        lst.append("0" * (zero_num - one_num))
                    zero_num = 0
                    one_num = 1
                else:
                    one_num += 1
            else:
                zero_num += 1
        else:
            if zero_num < one_num:
                lst.append("1" * (one_num - zero_num))
                lst.append("Sub")
                sub_lst.append("1" * zero_num + "0" * zero_num)
            elif zero_num == one_num:
                lst.append("Sub")
                sub_lst.append("1" * zero_num + "0" * zero_num)
            else:
                lst.append("Sub")
                sub_lst.append("1" * one_num + "0" * one_num)
                lst.append("0" * (zero_num - one_num))

        # 排序所有子序列
        sub_lst.sort(reverse=True)

        # 将排序后的子序列填入到主序列中
        i1 = 0
        i2 = 0
        while i1 < len(lst) and i2 < len(sub_lst):
            if lst[i1] == "Sub":
                lst[i1] = sub_lst[i2]
                i2 += 1
            i1 += 1

        # 合并并返回主序列
        return "".join(lst)


if __name__ == "__main__":
    print(Solution().makeLargestSpecial(S="11011000"))  # "11100100"
