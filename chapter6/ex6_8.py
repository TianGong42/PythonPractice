# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，
# 包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来
pet1 = {'name':'小黄' , 'master':'张三'}
pet2 = {'name':'多尔衮', 'master':'李四'}
pet3 = {'name':'康熙', 'master':'王五'}
pets = [pet1, pet2, pet3]
for pet in pets:
    print("这宠物的名字叫： " + pet['name'] + " 主人的名字： " + pet['master'])