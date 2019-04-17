N, M = map(int, input().split())

shops = []
min_money = 0

for i in range(0, N):
    A, B = map(int, input().split())

    shops.append({'price': A, 'stock': B})

shops.sort(key=lambda x: x['price'])

for shop in shops:

    # 在庫がある
    if M < shop['stock']:
        min_money += shop['price'] * M
        break
    else:
        min_money += shop['price'] * shop['stock']
        M -= shop['stock']

print(min_money)
