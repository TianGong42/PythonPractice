# 创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt'。
revers = {'nile':'egype','长江':'中国','黄河':'中国'}

for rever, country in revers.items():
    print("The " + rever + "runs through " + country)
for rever in revers.keys():
    print(rever)

for country in revers.values():
    print(country)