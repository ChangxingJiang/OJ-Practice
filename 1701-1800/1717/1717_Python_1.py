class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        lst = [""]
        for ch in s:
            if ch == "a" or ch == "b":
                lst[-1] += ch
            else:
                if lst[-1] != "":
                    lst.append("")

        ans = 0

        for ss in lst:
            # 计算总数的最大值
            max_num = min(ss.count("a"), ss.count("b"))

            if x >= y:
                # 计算ab数量的最大值
                max_n1 = 0
                count = 0
                for ch in ss:
                    if ch == "a":
                        count += 1
                    else:
                        if count > 0:
                            count -= 1
                            max_n1 += 1

                # 计算最终结果
                ans += max_n1 * x + (max_num - max_n1) * y

            else:
                # 计算ba数量的最大值
                max_n2 = 0
                count = 0
                for ch in ss:
                    if ch == "b":
                        count += 1
                    else:
                        if count > 0:
                            count -= 1
                            max_n2 += 1

                # 计算最终结果
                ans += max_n2 * y + (max_num - max_n2) * x

        return ans


if __name__ == "__main__":
    print(Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5))  # 19
    print(Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4))  # 20

    # 382920
    print(Solution().maximumGain(
        s="abbmzgaabtaabsbabhaahabnaeabdbaababbbiabaavababtabwbababzbdabbaaabhbyabdvabbaabbquapaaaaqbbblbuaawlnbbaxaubbbbbpbabbbpaaaacbbaabaaaahbbcoyaauabanqaabpbbbgaawbhabbbbaobsaaababbafbababbbbaaaqbabsbsmabbxqylbbbba",
        x=9421, y=8003))
