

# class Grandfather:
#     def show_grandfather(self):
#         print("Grandfather")

# class Father(Grandfather):
#     def show_father(self):
#         print("Father")

# class Son(Father):
#     def show_son(self):
#         print("Son")

# s = Son()
# s.show_grandfather()
# s.show_father()
# s.show_son()



class Grandfather:
    def __init__(self):
        self.public_money = 100000       
        self._protected_land = 5         
        self.__private_gold = 10        

    def show_grandfather(self):
        print("Public Money:", self.public_money)
        print("Protected Land:", self._protected_land)
        print("Private Gold:", self.__private_gold)


class Father(Grandfather):
    def show_father(self):
        # Public member can be accessed
        print("Father accesses Public Money:", self.public_money)

        # Protected member can be accessed
        print("Father accesses Protected Land:", self._protected_land)

        # Private member cannot be accessed directly
        # print(self.__private_gold)  # Error


class Son(Father):
    def show_son(self):
        # Public member
        print("Son accesses Public Money:", self.public_money)

        # Protected member
        print("Son accesses Protected Land:", self._protected_land)

        # Private member cannot be accessed directly
        # print(self.__private_gold)  # Error


s = Son()

s.show_grandfather()
s.show_father()
s.show_son()

# Public member can be accessed outside the class
print("Outside - Public Money:", s.public_money)

# Protected member can technically be accessed in Python,
# but it should not be accessed directly.
print("Outside - Protected Land:", s._protected_land)

# Private member cannot be accessed directly
# print(s.__private_gold)  # AttributeError
