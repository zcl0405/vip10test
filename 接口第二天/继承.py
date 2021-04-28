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
#多继承的意思是一个类同时继承了多个父类,当一个类有多个父类时,默认使用第一个父类同名的属性和方法,同名的
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

#子类重写父类同名属性和方法,子类和父类具有同名的属性和方法时,默认使用子类的同名的属性和方法
class Master();
    def __init__(self):



#多肽

