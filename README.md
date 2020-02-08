

# 第二章 变量和简单数据类型
### 2.3.1 修改字符串的大小写
- lower()函数，所有字母修改为小写
- upper()函数，所有字母修改为大写
- title()函数，每个单词首字母大写
### 2.3.4 删除空白
- rstrip()函数，删除字符串末尾处的空白
- lstrip()函数，删除字符串开头处的空白
- strip()函数，删除字符串两端的空白

# 第三章：列表简介



### 3.2.2 在列表中添加函数
append()函数:在list末尾会添加一个元素
insert()函数：在列表任何位置添加新元素 insert(1, '新元素'),在位置为1的位置增加一个新元素，剩余元素右移

### 3.2.3 在列表中删除元素
del函数，根据索引删除列表中的元素
`del list[0]` 这样就是删除list[0]的元素，

pop()函数：将列表中的最后一个元素删除，并且使用它。也可以删除指定位置的元素
所以pop()函数的用法有，`pop()和pop(1)`

remove()函数：按值删除list中的元素，如果lsit中有多个相同的元素，只会删除第一个  

### 3.3.1使用sort方法进行排序
sort()函数：按照字母顺序进行排序,从a开始
sort(reverse=True):按照字母顺序进行排序，倒叙
备注：上述排序完成后固定在list中

### 3.3.2使用sorted()方法进行临时排序
使用sorted()函数会对list做临时排序，并且做出一个输出。但是不影响list中元素的排序
使用方式sorted(list)

### 3.3.3倒叙打印列表
reverse()函数：反转列表元素的排列顺序
cars.reverse()

# 第四章：操作列表
### 4.3.1 使用函数range()
range()函数可以生成一系列数字
可使用函数list()将range()的结果直接转换为列表
如list(range(1,5))
range()函数还可以指定步长，例如，打印1~10内的偶数。list(range(2,11,2))

### 4.3.3 对数字列表执行简单的统计计算
min()
max()
sum()

### 4.3.4列表解析
`squares = [value**2 for value in range(1,11)]`
首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到
列表中的值。在这个示例中，表达式为value**2,它计算平方值。然后使用一个for循环，用于给表达式提供值.
在上述示例中，for循环为for value in range(1,11),它将值1~10提供表达式value**2

### 使用列表的一部分
### 4.4.1 切片
要创建切片，可指定要使用的第一个元素和最后一个元素的索引，与函数range一样
`numbers[0:3]`将输出0、1、2位置的元素
- 没有指定索引，将从头开始`numbers[:4]`
- 要让索引终止于列表末尾`numbers[2:]`
- 输出最后三个元素`numbers[-3:]`

### 4.4.3复制列表
复制列表做一个副本，需要以下方式 number1 = number2[:]
这样number2才能做单独的副本存在

## 4.5元组
Python将不能修改的值称为不可变的，而不可变的列表称为列表
虽然不能修改元组的元素，但是可以给存储元组的变量赋值。

# 第六章：字典
字典是一系列键值对
### 6.2.1 访问字典中的值
要获取与键相关联的值，可一次指定字典名和放在方括号内的键

### 6.2.5 删除键值对
```
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)
```

### 6.3.1遍历所有的键值-对
`for key, value in user_0.items():`

### 6.3.2 遍历所有键
`for name in favorite_languages.keys():`
上述方式使用keys()函数来获取键，也可以使用

### 6.3.4遍历字典中的所有值
`for language in favorite_languages.values():`

# 第8章：函数
###8.1.2 实参和形参
在定义函数greet_user()中，username是一个形参，函数完成其工作所需的一项信息
suye是一个实参，实参是调用函数时传给函数的信息。
```
def greet_user(username):
    """显示简单的问候语"""
    print("Hello," + username.title() + "!")
greet_user('suye')
```

### 8.2.1 位置实参
调用函数时，Python必须将函数调用中的每个实参关联到函数定义中的一个形参。
最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参

### 8.2.2 关键字实参
关键字实参是在实参中将名称和值关联起来。因此向函数传递实参时不会混淆
所以关键字实参的顺序无关紧要
`describe_pet(animal_type='hamster', pet_name = 'harry')`
### 8.4.2 禁止修改列表
有时候，需要禁止函数修改列表
为了解决这个问题，可向函数传递列表的副本而不是原件
这样函数所做的任何修改都只影响副本，而丝毫不影响原件
```function_name(list_name[:])```

## 8.5 传递任意数量的实参
有时候，你预先不知道函数需要接受多少个实参，但python允许函数从调用语句中收集
任意数量的实参
```
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
形参名*toppings中的星号让Python创建一个名为toppings的空元组,
并将受到的所有值都封装到这个元组中



