from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0  # 5美元的数量
        ten = 0  # 10美元的数量

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if ten < 1:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                else:
                    if five < 1:
                        return False
                    else:
                        five -= 1
                        ten -= 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().lemonadeChange([5, 5, 5, 10, 20]))  # True
    print(Solution().lemonadeChange([5, 5, 10]))  # True
    print(Solution().lemonadeChange([10, 10]))  # False
    print(Solution().lemonadeChange([5, 5, 10, 10, 20]))  # False
