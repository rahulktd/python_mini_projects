# Maximum profit by buying and selling a share at most twice

# In daily share trading, a buyer buys shares in the morning and sells them on the same day.
# If the trader is allowed to make at most 2 transactions in a day,
# the second transaction can only start after the first one is complete (Buy->sell->Buy->sell).
# Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

# Input:   price[] = {10, 22, 5, 75, 65, 80}
# Output:  87
# Trader earns 87 as sum of 12, 75
# Buy at 10, sell at 22,
# Buy at 5 and sell at 80

prices = [10, 22, 5, 75, 65, 80]
n = len(prices)
profit = [0]*n
max_price = prices[n-1]

for i in range(n-2,0,-1):
    if prices[i]>max_price:
        max_price = prices[i]

    profit[i] = max(profit[i+1],max_price-prices[i])

min_price = prices[0]

for i in range(1,n):
    if prices[i] < min_price:
        min_price = prices[i]
    profit[i] = max(profit[i-1],profit[i]+(prices[i]-min_price))

result = profit[n-1]
print(result)