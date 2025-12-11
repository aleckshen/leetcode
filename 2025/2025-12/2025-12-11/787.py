class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = list(prices)

            for node, dest, price in flights:
                if prices[node] == float('inf'):
                    continue
                if prices[node] + price < tempPrices[dest]:
                    tempPrices[dest] = prices[node] + price

            prices = tempPrices

        if prices[dst] == float('inf'):
            return -1
        return prices[dst]