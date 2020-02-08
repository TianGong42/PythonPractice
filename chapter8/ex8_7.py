#编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
def make_album(singer, album):
    singer_album = {"singer":singer, "album":album}
    return singer_album
print(make_album("suye","前任"))
while True:
    print("请按q退出程序")
    singer = input("请输入歌手的名字:")
    if singer == 'q':
        break
    album = input("请输入专辑名字：")
    if album == 'q':
        break
    print(make_album(singer,album))