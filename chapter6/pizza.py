# 在字典中存储列表
# 存储所有点披萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
# 概述所有点的披萨 个人感觉和二维数组一样
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)