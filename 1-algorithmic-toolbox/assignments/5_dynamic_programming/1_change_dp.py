def change(money, denominations):
    min_coins = [0]*(money+1)
    min_coins[0] = 0
    for m in range(1, money+1):
        min_coins[m] = float('inf')
        for coin in denominations:
            if m >= coin:
                num_coins = min_coins[m-coin]+1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m, [1, 3, 4]))
