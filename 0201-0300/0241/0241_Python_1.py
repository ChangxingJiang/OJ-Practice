from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 处理只剩下数字的情况
        if input.isdigit():
            return [int(input)]

        # 处理还剩下数字和运算符的情况
        ans = []
        for i, ch in enumerate(input):
            if ch in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for n1 in left:
                    for n2 in right:
                        if ch == "+":
                            ans.append(n1 + n2)
                        elif ch == "-":
                            ans.append(n1 - n2)
                        else:
                            ans.append(n1 * n2)
        return ans


if __name__ == "__main__":
    # [0, 2]
    print(Solution().diffWaysToCompute("2-1-1"))

    # [-34, -14, -10, -10, 10]
    print(Solution().diffWaysToCompute("2*3-4*5"))
