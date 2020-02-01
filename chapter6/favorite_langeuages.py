favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',    # 最后一行的逗号可加可不加
}
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + ".")
for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")
names = ['jen','phil','张三','李四']
for name in names:
    if name in favorite_languages.keys():
        print("谢谢参加调查")
    else:
        print("您还没有参加调查")