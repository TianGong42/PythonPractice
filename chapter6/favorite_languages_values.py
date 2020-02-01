# 遍历字段中的所有值
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',    
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())