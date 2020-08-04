from typing import List


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().basicCalculatorIV(expression="e + 8 - a + 5", evalvars=["e"], evalints=[1]))  # ["-1*a","14"]
    print(Solution().basicCalculatorIV(expression="e - 8 + temperature - pressure",
                                       evalvars=["e", "temperature"], evalints=[1, 12]))  # ["-1*pressure","5"]
    print(Solution().basicCalculatorIV(expression="(e + 8) * (e - 8)", evalvars=[], evalints=[]))  # ["1*e*e","-64"]
    print(Solution().basicCalculatorIV(expression="7 - 7", evalvars=[], evalints=[]))  # []
    print(Solution().basicCalculatorIV(expression="a * b * c + b * a * c * 4", evalvars=[], evalints=[]))  # ["5*a*b*c"]
    print(
        Solution().basicCalculatorIV(expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                                     evalvars=[],
                                     evalints=[]))  # ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
