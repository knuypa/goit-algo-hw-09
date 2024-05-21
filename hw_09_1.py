
# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Жинамічне програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [None] * (amount + 1)
    coin_count[0] = {}

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                if coin_count[x - coin] is not None:
                    coin_count[x] = coin_count[x - coin].copy()
                    if coin in coin_count[x]:
                        coin_count[x][coin] += 1
                    else:
                        coin_count[x][coin] = 1
                else:
                    coin_count[x] = {coin: 1}

    return coin_count[amount] if coin_count[amount] is not None else {}

# Тести
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(113))     # {1: 1, 2: 1, 10: 1, 50: 2}