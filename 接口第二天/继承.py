'''
面向对象的继承是指多个类之间的所属关系,即子类默认继承父类所有的方法和属性
在python中所有类默认继承object类,object类是顶级类或基类,其他子类叫做派生类
'''
# class A(object):#f父类
#     def __init__(self):
#         self.num=1
#     def info_print(self):
#         print(self.num)
# class B(A):
#     pass
# result=B()
# result.info_print()
# #单继承
# class Master():
#     def __init__(self):
#         self.gongfu='五香煎饼果子配方'
#     def make_cake(self):
#         print(f'运用{self.gongfu}制作煎饼果子')
# class Tudi(Master):
#     pass
# xiaoming=Tudi()#创建对象
# xiaoming.gongfu#Tudi是子类继承了Master父类的属性和方法,所以xiaoming可以调用Master的属性
# xiaoming.make_cake()#xiaoming可以调用父类的方法
'''
多继承的意思是一个类同时继承了多个父类,当一个类有多个父类时,默认使用第一个父类同名的属性和方法,同名的
'''
# class Master():
#     def __init__(self):
#         self.gongfu='五香煎饼果子配方'
#     def make_cake(self):
#         print(f'运用{self.gongfu}制作煎饼果子')
# class school():
#     def __init__(self):
#         self.gongfu='香辣煎饼果子的配方'
#     def make_cake(self):
#         print(f'运用{self.gongfu}制作煎饼果子')
#     def make_cake2(self):
#         print(222222)
# class Tudi(Master,school):
#       pass
# xiaoming=Tudi()
# print(xiaoming.gongfu)
# xiaoming.make_cake()
# xiaoming.make_cake2()

'''
子类重写父类同名属性和方法,子类和父
类具有同名的属性和方法时,默认使用子类的同名的属性和方法
'''
# class Master():
#     def __init__(self):
#         self.gongfu='五香果子煎饼配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}的方法制作煎饼果子')
# class tudi(Master):
#     def __init__(self):
#         self.gongfu='独创煎饼果子配方'
#     def make_cake(self):
#         print('用独创的配方制作煎饼果子')
#
# xiaoming=tudi()
# print(xiaoming.gongfu)
# xiaoming.make_cake()

'''子类调用父类同名的方法和属性'''
# class Master():
#     def __init__(self):
#         self.gongfu = '五香煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}煎饼果子配方做煎饼果子')
# class school():
#     def __init__(self):
#         self.gongfu = '香辣煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}煎饼果子配方制作煎饼果子')
# class tudi(Master,school):
#     def __init__(self):
#         self.gongfu = '独创的煎饼果子配方'
#     def make_cake(self):
#         self.__init__()#如果是先调用父类的属性和方法,父类属性会覆盖子类属性顾在调用属性前先调用自己子类的初始化
#         print(f'用{self.gongfu}的方式制作煎饼果子')
#         #调用父类的方法但是为了保证调用到的也是父类的属性必须在调用前调用父类的初始化
#     def master_make_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def school_make_cake(self):
#         school.__init__(self)
#         school.make_cake(self)
# xiaoming=tudi()
# xiaoming.make_cake()
# xiaoming.master_make_cake()
# xiaoming.school_make_cake()
# xiaoming.make_cake()
'''
多层继承
'''
# class Master():
#     def __init__(self):
#         self.gongfu='香辣煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}制作煎饼果子')
# class School():
#     def __init__(self):
#         self.gongfu='五香煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}制作煎饼果子')
# class tudi(Master,School):
#     def __init__(self):
#         self.gongfu='独创煎饼果子配方'
#     def make_cake(self):
#         self.__init__()
#         print(f'用{self.gongfu}制作煎饼果子')
#     def master_make_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def school_make_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
# class tusun(tudi):
#     pass
# xiaoming=tudi()
# xiaoming.school_make_cake()
# xiaogang=tusun()
# xiaogang.school_make_cake()
# xiaogang.make_cake()
# xiaogang.master_make_cake()
'''
super()调用父类方法
'''
# class Master():
#     def __init__(self):
#         self.gongfu='香辣煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}制作煎饼果子')
#
# class school(Master):
#     def __init__(self):
#         self.gongfu='五香煎饼果子配方'
#     def make_cake(self):
#         print(f'用{self.gongfu}制作煎饼果子')
# class tudi(school):
#     def __init__(self):
#         self.gongfu='独创煎饼果子配方'
#     def make_cake(self):
#         self.__init__()
#         print(f'用{self.gongfu}制作煎饼果子')
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()

# xiaoming=tudi()
# xiaoming.make_old_cake()
'''
在python中可以为实例属性和方法设置私有权限,即设置某个实例属性或者实例方法不继承给子类
设置私有权限的方法:在属性名和方法名前面加上2个下划线__
'''
# class Master():
#     def __init__(self):
#         self.gongfu='五香煎饼果子的配方'
#     def make_cake(self):
#         print(f'运用{self.gongfu}制作煎饼果子')
# class school():
#     def __init__(self):
#         self.gongfu='黑马煎饼果子配方'
#     def make_cake(self):
#         print(f'运用{self.gongfu}制作煎饼果子')
# class tudi():
#     def __init__(self):
#         self.gongfu='独创煎饼果子配方'
#         self.__money=200#定义私有属性
#     def __info_print(self):#定义私有方法
#         print(self.gongfu)
#         print(self.__money)
#     def make_cake(self):
#         self.__init__()
#         print(f'运用{self.gongfu}制作煎饼果子')
# class tusun(tudi):
#     pass
# xiaom=tudi()
# xiaom.__info_print()
# print(xiaom.__money)
# xiaog=tusun()
# print(xiaog.__money)
'''
在Python中一般定义函数get_xx用来获取私有属性,定义set_用来修改私有属性值
'''
class Master():
    def __init__(self):
        self.gongfu='五香煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.gongfu}制作煎饼果子')
class school():
    def __init__(self):
        self.gongfu='香辣煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.gongfu}制作煎饼果子')
class tudi(Master,school):
    def __init__(self):
        self.kongfu='独创煎饼果子的配方'
        self.__money=200#定义私有属性
    def get__money(self):#获取私有属性
        return self.__money
    def set__money(self):#修改私有属性
        self.__money=500
class tusun(tudi):
    pass
xiaom=tudi()
xiaog=tusun()
print(xiaog.get__money())
xiaog.set__money()
print(xiaog.get__money())

