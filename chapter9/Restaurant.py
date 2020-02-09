class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """表述餐厅的方法"""
        print("餐厅的名字是" + self.restaurant_name)
        print("餐厅的类型是" + self.cuisine_type)
    def open_restaurant(self):
        """打印餐厅的营业状态"""
        print("现在正常营业呢")
    def show_number_served(self):
        """打印有多少人被这家餐厅服务过"""
        print("有" + str(self.number_served) + "在这家餐厅就餐过")
    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served
    def increment_number_served(self, number):
        """每次增加的就餐人数"""
        if number < 0:
            print("就餐人数不能是负数喔")
        else:
            self.number_served += number
hdl = Restaurant("海底捞","火锅")
print(hdl.restaurant_name)
print(hdl.cuisine_type)
hdl.describe_restaurant()
hdl.open_restaurant()
hdl.show_number_served()
hdl.set_number_served(10)
hdl.show_number_served()
hdl.increment_number_served(10)
hdl.show_number_served()
hdl.increment_number_served(-10)


