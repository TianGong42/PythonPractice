favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',    # 最后一行的逗号可加可不加
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + 
        ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")