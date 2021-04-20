# class washer():#定义类
#     def wash(self):
#         print('我会洗衣服')
# haier1=washer()#创建对象
# print(haier1)
# haier1.wash()#haier对象调用实例方法,创建对象的过程也叫实例化对象

# class washer():
#     def print_info(self):
#         print(f'haire1洗衣机的宽度是{self.width}')
#
#
# haier1 = washer()
# haier1.width = 500
# haier2=washer()
# haier2.width=600
#
#
# haier1.print_info()
# haier2.print_info()

# class washer():
#     def __init__(self):
#         self.width=500
#         self.height=800
#     def print_info(self):
#         print(f'洗衣机的宽度是{self.width}')
#         print(f'洗衣机的高度是{self.height}')
# haier1=washer()
# haier1.print_info()

class Washer():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')
haier1=Washer(10,20)
haier1.print_info()
#
# haier2=Washer(30,40)
# haier2.print_info()





'''
定义一个老师类,
老师的属性有:姓名.性别,教的课程
方法:可以教学
'''
# class Teacher():
#     def tea_math(self):
# teacher1.

# class Furniture():
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
# class Home():
#     def __init__(self,address,area):
#         self.address=address
#         self.area=area
#         self.free_area=area
#         self.furniture=[]
#     def __str__(self):
#         return f'房子坐落于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'
#     def add_furniture(self,item):
#         if self.free_area>=item.area:
#             self.furniture.append(item.name)
#             self.free_area=self.free_area-
