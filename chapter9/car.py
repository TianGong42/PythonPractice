class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值
            禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能往回拨里程表！")
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
class Battery():
    """一次模拟电动汽车的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270 
        message = "这车大概可以行使 " + str(range)
        message += " 公里在整个里程."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
class ElectricCar(Car):
    """
    电动车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
"""
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())       
my_new_car.read_odometer() 
print("将里程修改为23")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("将里程修改为22")
my_new_car.update_odometer(22)
my_new_car.read_odometer()
print("增加100里程")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
print("--------我是高贵的分割线---------------")
my_tesal = ElectricCar('tesla', 'model s', 2016)
print(my_tesal.get_descriptive_name())    # 直接调用父类的方法
my_tesal.battery.describe_battery()
my_tesal.battery.get_range()
my_tesal.battery.upgrade_battery()
my_tesal.battery.get_range()
"""