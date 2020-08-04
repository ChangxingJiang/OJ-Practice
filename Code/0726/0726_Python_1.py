from collections import Counter


class Solution:
    def __init__(self):
        self.idx = 0
        self.formula = ""
        self.N = 0

    def resolver(self):
        count = Counter()
        while self.idx < self.N and self.formula[self.idx] != ")":
            # 当前字符为大写字母的情况
            if self.formula[self.idx].isupper():
                # 获取原子名称
                idx_start = self.idx
                self.idx += 1
                while self.idx < self.N and self.formula[self.idx].islower():  # 找到所有连续的小写字母（即完整原子名）
                    self.idx += 1
                name = self.formula[idx_start:self.idx]

                # 获取并累加原子数量
                i_start = self.idx
                while self.idx < self.N and self.formula[self.idx].isdigit():
                    self.idx += 1
                count[name] += int(self.formula[i_start:self.idx] or 1)

            # 当前字符为左括号的情况
            elif self.formula[self.idx] == "(":
                self.idx += 1
                inner_count = self.resolver()
                for name, value in inner_count.items():
                    count[name] += value

        self.idx += 1

        # 处理括号结束后的洗漱
        i_start = self.idx
        while self.idx < self.N and self.formula[self.idx].isdigit():
            self.idx += 1
        rate = int(self.formula[i_start:self.idx] or 1)
        if rate > 1:
            for name in count:
                count[name] *= rate

        return count

    def countOfAtoms(self, formula: str) -> str:
        self.formula = formula
        self.N = len(formula)

        # 解析化学式
        count = self.resolver()

        # 排序并输出
        ans = []
        for name in sorted(count):
            ans.append(name)
            rate = count[name]
            if rate > 1:
                ans.append(str(rate))
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().countOfAtoms(formula="H2O"))  # "H2O"
    print(Solution().countOfAtoms(formula="Mg(OH)2"))  # "H2MgO2"
    print(Solution().countOfAtoms(formula="K4(ON(SO3)2)2"))  # "K4N2O14S4"
    print(Solution().countOfAtoms(formula="Be32"))  # "Be32"
    print(Solution().countOfAtoms(formula="(NB3)33"))  # "NB99"
