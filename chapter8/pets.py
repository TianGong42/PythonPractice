def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".") 
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')  # 仓鼠,harry
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')   # harry,仓鼠 参数的位置很重要