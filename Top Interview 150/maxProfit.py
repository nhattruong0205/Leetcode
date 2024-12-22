def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # Initialize min_price to a large value
    min_price = float('inf')  
    # Initialize max_profit to 0
    max_profit = 0          

    for price in prices:
        if price < min_price:
            # Update min_price if a lower price is found
            min_price = price  
        elif price - min_price > max_profit:
            # Update max_profit if a higher profit is found
            max_profit = price - min_price

    # Return the maximum profit found
    return max_profit