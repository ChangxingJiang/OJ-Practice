class Solution:
    def maxDiff(self, num: int) -> int:
        num_max = num_min = str(num)

        # 计算替换后的最大值
        for ch in num_max:
            if ch != "9":
                num_max = num_max.replace(ch, "9")
                break

        # 计算替换后的最小值
        first_num = num_min[0]
        for i, ch in enumerate(num_min):
            if i == 0:
                if ch != "1":
                    num_min = num_min.replace(ch, "1")
                    break
            elif ch != "0" and ch != first_num:
                num_min = num_min.replace(ch, "0")
                break

        return int(num_max) - int(num_min)


if __name__ == "__main__":
    print(Solution().maxDiff(555))  # 888
    print(Solution().maxDiff(9))  # 8
    print(Solution().maxDiff(123456))  # 820000
    print(Solution().maxDiff(10000))  # 80000
    print(Solution().maxDiff(9288))  # 8700
    print(Solution().maxDiff(111))  # 8700
