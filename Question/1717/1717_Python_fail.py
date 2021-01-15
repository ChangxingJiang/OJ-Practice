class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # 统计每一个只有ab的子串的信息
        lst = []
        a_num, b_num = 0, 0  # a的数量、b的数量
        start_ch, start_num = "", 0  # 开始的字符，开始字符的数量
        end_ch, end_num = "", 0  # 结束的字符，结束字符的数量
        for ch in s:
            if ch == "a":
                if a_num == 0 and b_num == 0:
                    start_ch, start_num = "a", 1
                elif start_ch == "a" and a_num == start_num and b_num == 0:
                    start_num += 1
                a_num += 1
                if end_ch != "a":
                    end_ch, end_num = "a", 1
                else:
                    end_num += 1
            elif ch == "b":
                if a_num == 0 and b_num == 0:
                    start_ch, start_num = "b", 1
                elif start_ch == "b" and b_num == start_num and a_num == 0:
                    start_num += 1
                b_num += 1
                if end_ch != "b":
                    end_ch, end_num = "b", 1
                else:
                    end_num += 1
            else:
                if a_num != 0 and b_num != 0:  # 如果子串中既有a也有b，则存储这个子串
                    lst.append((a_num, b_num, start_ch, start_num, end_ch, end_num))

                # 结束上一个子串
                a_num, b_num = 0, 0
                start_ch, start_num = "", 0
                end_ch, end_num = "", 0
        if a_num != 0 and b_num != 0:  # 如果子串中既有a也有b，则存储这个子串
            lst.append((a_num, b_num, start_ch, start_num, end_ch, end_num))

        ans = 0

        for a_num, b_num, start_ch, start_num, end_ch, end_num in lst:
            # 计算每一个段落中ab和ba的最大值
            max_num = min(a_num, b_num)  # 计算总数的最大值
            max_n1 = min(a_num - (end_num if end_ch == "a" else 0),
                         b_num - (start_num if start_ch == "b" else 0))  # 计算ab数量的最大值
            max_n2 = min(a_num - (start_num if start_ch == "a" else 0),
                         b_num - (end_num if end_ch == "b" else 0))  # 计算ba数量的最大值

            print(a_num, b_num, start_ch, start_num, end_ch, end_num, "->", max_num, max_n1, max_n2, "->",
                  max_n1 * x + (max_num - max_n1) * y if x >= y else max_n2 * y + (max_num - max_n2) * x)

            # 计算最终解
            if x >= y:
                ans += max_n1 * x + (max_num - max_n1) * y
            else:
                ans += max_n2 * y + (max_num - max_n2) * x

        return ans


if __name__ == "__main__":
    print(Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5))  # 19
    print(Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4))  # 20

    # 382920
    print(Solution().maximumGain(
        s="abbmzgaabtaabsbabhaahabnaeabdbaababbbiabaavababtabwbababzbdabbaaabhbyabdvabbaabbquapaaaaqbbblbuaawlnbbaxaubbbbbpbabbbpaaaacbbaabaaaahbbcoyaauabanqaabpbbbgaawbhabbbbaobsaaababbafbababbbbaaaqbabsbsmabbxqylbbbba",
        x=9421, y=8003))
