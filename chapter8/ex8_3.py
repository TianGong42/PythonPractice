# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。
def make_shirt(size, word = "I love Python"):
    print("这件T恤的尺码是" + size + ", 它上面写了" + word)

make_shirt("m")
make_shirt("xxl","今天不减肥")