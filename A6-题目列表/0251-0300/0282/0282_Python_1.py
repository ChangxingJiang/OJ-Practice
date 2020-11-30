from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().addOperators(num="123", target=6))  # ["1+2+3", "1*2*3"]
    print(Solution().addOperators(num="232", target=8))  # ["2*3+2", "2+3*2"]
    print(Solution().addOperators(num="105", target=5))  # ["1*0+5","10-5"]
    print(Solution().addOperators(num="00", target=0))  # ["0+0", "0-0", "0*0"]
    print(Solution().addOperators(num="3456237490", target=9191))  # []
