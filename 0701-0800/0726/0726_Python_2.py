from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        N = len(formula)
        stack = [Counter()]
        i = 0
        while i < N:
            # 当前字符为大写字母的情况
            if formula[i].isupper():
                # 获取原子名称
                idx_start = i
                i += 1
                while i < N and formula[i].islower():  # 找到所有连续的小写字母（即完整原子名）
                    i += 1
                name = formula[idx_start:i]

                # 获取并累加原子数量
                idx_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                stack[-1][name] += int(formula[idx_start:i] or 1)

            # 当前字符为左括号的情况
            elif formula[i] == "(":
                stack.append(Counter())
                i += 1

            elif formula[i] == ")":
                inner = stack.pop()
                i += 1
                idx_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                rate = int(formula[idx_start:i] or 1)
                for name, value in inner.items():
                    stack[-1][name] += value * rate

        # 排序并输出
        count = stack[0]
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
