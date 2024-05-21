import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

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

def measure_time(func, amount):
    start_time = time.time()
    result = func(amount)
    end_time = time.time()
    return result, end_time - start_time

# Приклади сум для тестування
amounts = [113, 500, 1000, 5000, 10000]

# Вимірювання часу для жадібного алгоритму
print("Greedy Algorithm:")
for amount in amounts:
    result, exec_time = measure_time(find_coins_greedy, amount)
    print(f"Amount: {amount}, Time: {exec_time:.6f} seconds, Result: {result}")

# Вимірювання часу для алгоритму динамічного програмування
print("Dynamic Programming Algorithm:")
for amount in amounts:
    result, exec_time = measure_time(find_min_coins, amount)
    print(f"Amount: {amount}, Time: {exec_time:.6f} seconds, Result: {result}")