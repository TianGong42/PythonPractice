#编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为City, Country的字符串，如Santiago, Chile。
# 将这个函数存储在一个名为city_functions.py的模块中。
def city_functions(city, country, population=""):
    if population:
        city_country = city + ', ' + country + '-population' + str(population)
    else:
        city_country = city + ', ' + country 
    return city_country
print(city_functions('Santiago', 'chile',5000000))