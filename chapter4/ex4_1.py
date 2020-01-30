# 想出至少三种你喜欢的比萨，将其名称存储在一个列表中，
# 再使用for循环将每种比萨的名称都打印出来。
pizzas = ['牛肉','海鲜','芝士']
for pizza in pizzas:
    print("我喜欢" + pizza)
print("我实在喜欢披萨")
friend_pizzas = pizzas[:]
pizzas.append("猪肉")
friend_pizzas.append("驴肉")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My firend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)