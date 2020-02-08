# 创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(magicians_names):
    for magicians_name in magicians_names:
        print(magicians_name)
def make_great(magicians_names):
    names = []
    for magicians_name in magicians_names:
        magicians_name = "the Great " + magicians_name
        names.append(magicians_name)
    return names
    
names = ['suye','刘谦','大卫']
show_magicians(names[:])
names = make_great(names)
show_magicians(names)
