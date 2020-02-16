filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip() 
print(pi_string)
print(len(pi_string))

pi_string = ''
for line in lines:
    pi_string += line.strip() # 和上面的区别，一个是去除左边，一个是去除右边的空格
print(pi_string)
print(len(pi_string))