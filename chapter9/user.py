class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.long_attempts = 0
    def describe_user(self):
        print(self.first_name + " " + self.last_name)
    def greet_user(self):
        print("Hi," + self.first_name + " " + self.last_name)
    def increment_login_attempts(self):
        """登录次数加一"""
        self.long_attempts += 1
    def reset_login_attempts(self):
        """重置登录次数"""
        self.long_attempts = 0
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []
    def show_privileges(self):
        print("打印权限狗的权限")
        for power in self.privileges:
            print(power)

suye = User("su","ye")
suye.describe_user()
suye.greet_user()
print(suye.long_attempts)
suye.increment_login_attempts()
print(suye.long_attempts)
suye.reset_login_attempts()
print(suye.long_attempts)
print("----------打印权限狗的分割线-------------")
admin = Admin("admin","123456")
admin.privileges = ["删帖","封号"]
admin.show_privileges()



    