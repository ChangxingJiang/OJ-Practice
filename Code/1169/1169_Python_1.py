import collections
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 依据人名重新分组交易记录
        # 时间复杂度：O(N)
        transactions_by_name = collections.defaultdict(list)
        for transaction in transactions:
            name, time, money, city = transaction.split(",")
            transactions_by_name[name].append((int(time), city, int(money)))

        ans = set()

        # 依据各组人名分别排序并检查记录
        for name, transactions in transactions_by_name.items():
            transactions.sort()
            for i in range(len(transactions)):
                time1, city1, money1 = transactions[i]
                if money1 > 1000:
                    ans.add(",".join([name, str(time1), str(money1), city1]))
                for j in range(i + 1, len(transactions)):
                    time2, city2, money2 = transactions[j]
                    if time2 - time1 > 60:
                        break
                    if city1 != city2:
                        ans.add(",".join([name, str(time1), str(money1), city1]))
                        ans.add(",".join([name, str(time2), str(money2), city2]))

        return list(ans)


if __name__ == "__main__":
    # ["alice,20,800,mtv","alice,50,100,beijing"]
    print(Solution().invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"]))

    # ["alice,50,1200,mtv"]
    print(Solution().invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"]))

    # ["bob,50,1200,mtv"]
    print(Solution().invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))

    # ["alex,741,1507,barcelona","xnova,683,1149,amsterdam","bob,52,1152,beijing","bob,137,1261,beijing"]
    print(Solution().invalidTransactions(
        ["alex,741,1507,barcelona", "xnova,683,1149,amsterdam", "bob,52,1152,beijing", "bob,137,1261,beijing", "bob,607,14,amsterdam",
         "bob,307,645,barcelona", "bob,220,105,beijing", "xnova,914,715,beijing", "alex,279,632,beijing"]))
