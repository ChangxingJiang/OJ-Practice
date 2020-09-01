class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        left_num = 0  # "1"的数量
        right_num = 0  # "0"的数量
        need_array = None  # 准备被交换的特殊序列
        need_idx = 0  # 需要被交换的特殊序列的起始坐标
        find_idx = 0  # 准备用来交换的特殊序列的起始坐标

        i = 0
        while i < len(S):
            # print(S, i, "'" + S[i] + "'", "--", left_num, right_num, need_array, need_idx, find_idx)
            if not need_array:
                if S[i] == "1":
                    if right_num == 0:
                        left_num += 1
                    else:
                        need_idx = i - 2 * right_num
                        find_idx = i
                        need_array = S[need_idx:find_idx]
                        left_num = 1
                        right_num = 0
                else:
                    if left_num:
                        right_num += 1
                    if left_num < right_num:
                        left_num = 0
                        right_num = 0
            else:
                if S[i] == "1":
                    left_num += 1
                else:
                    right_num += 1
                    now_array = S[find_idx:i + 1]
                    if now_array > need_array:
                        if left_num == right_num:
                            S = S[:need_idx] + S[find_idx:i + 1] + S[need_idx:find_idx] + S[i + 1:]
                            return self.makeLargestSpecial(S)
                    if len(now_array) >= len(need_array) and now_array <= need_array:  # 找到的备换子序列不能提高字典序
                        left_num = 0
                        right_num = 0
                        i = find_idx - 1
                        need_array = None
                    if i == len(S) - 1 and len(now_array) < len(need_array):  # 处理已经检查到字符串末尾的情况
                        left_num = 0
                        right_num = 0
                        i = find_idx - 1
                        need_array = None
            # print(S, i, "'" + S[i] + "'", "->", left_num, right_num, need_array, need_idx, find_idx)
            i += 1
        return S


if __name__ == "__main__":
    print(Solution().makeLargestSpecial(S="11011000"))  # "11100100"
    print(Solution().makeLargestSpecial(S="110110100100"))  # "111010010100"
    print(Solution().makeLargestSpecial(S="1010101100"))  # "1100101010"
    print(Solution().makeLargestSpecial(S="1011111100000010101100"))  # "1111110000001100101010"
    print(Solution().makeLargestSpecial(S="101110110011010000"))  # "111101001100100010"
    print(Solution().makeLargestSpecial(S="11101001111001010000110010"))  # "11111001010001101000110010"
