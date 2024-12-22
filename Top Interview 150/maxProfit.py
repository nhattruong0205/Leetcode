def maxProfit(self,prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:

        # Check for the lowest current buy in
        min_price = min(min_price, price)


        profit = price - min_price
        
        # Check for the highest profit up to now
        max_profit = max(max_profit, profit)
    return max_profit