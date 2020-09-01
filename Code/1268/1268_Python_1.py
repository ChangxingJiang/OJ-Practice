from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        now_products = products
        for i, ch in enumerate(searchWord):
            new_products = []
            for product in now_products:
                if i < len(product) and product[i] == ch:
                    new_products.append(product)
            ans.append(new_products[:3])
            now_products = new_products
        return ans


if __name__ == "__main__":
    # [
    # ["mobile","moneypot","monitor"],
    # ["mobile","moneypot","monitor"],
    # ["mouse","mousepad"],
    # ["mouse","mousepad"],
    # ["mouse","mousepad"]
    # ]
    print(Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"))

    # [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    print(Solution().suggestedProducts(products=["havana"], searchWord="havana"))

    # [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
    print(Solution().suggestedProducts(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags"))

    # [[],[],[],[],[],[],[]]
    print(Solution().suggestedProducts(products=["havana"], searchWord="tatiana"))
