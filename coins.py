from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        results = {}
        return self.coinChangeDyn(coins, amount, results)

    def coinChangeDyn(self, coins, amount, results):
        if amount == 0:
            return 0
        elif amount in results:
            return results[amount]
        
        found = []
        for c in coins:
            if c > amount:
                pass
            else:
                recursed = self.coinChangeDyn(coins, amount-c, results)
                if recursed != -1:
                    found.append(recursed + 1)
        
        if len(found) == 0:
            result = -1
        else:
            result = min(found)

        results[amount] = result
        return result
