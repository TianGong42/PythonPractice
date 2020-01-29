motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('海螺')
print(motorcycles)
# 在列表中插入元素
motorcycles.insert(1,"酱油")
print(motorcycles)

# 在列表中删除元素
del motorcycles[0]
print("删除后的list：", end=" ")
print( motorcycles)
# pop()方法是删除列表最末尾的元素，并且使用这个元素
print(motorcycles.pop())
print("使用pop()方法后的list" , end= " ")
print(motorcycles)
motorcycles.remove("酱油")
print("使用remove()方法按值删除酱油元素后的list:" , end=" ")
print(motorcycles)