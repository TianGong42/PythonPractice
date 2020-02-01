pets = ['dog','cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:   # 这行代码是关键，如果list中有cat元素，就一直是true
    pets.remove('cat')   
print(pets)