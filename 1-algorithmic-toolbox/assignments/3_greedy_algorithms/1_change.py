def change(money):
    denominations = [10, 5, 1]
    if money == 0:
        return 0
    coins = 0
    while money > 0:
        diff = money-max(denominations)
        if diff >= 0:
            money = diff
            coins+=1
        else:
            denominations.remove(max(denominations))
    return coins

if __name__ == '__main__':
    m = int(input())
    print(change(m))
