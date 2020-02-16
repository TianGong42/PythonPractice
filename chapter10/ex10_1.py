# 
filename = 'learning_python.txt'
with open(filename,encoding='utf-8') as file_object:
    print(file_object.read().replace("Python","C"))
    for line in file_object.readlines():
        print(line.rstrip())
    lines = file_object.readlines()
for line in lines:
    print(line)