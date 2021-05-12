'''
面向对象的三大特性:封装,继承和多态
封装:将属性和方法写到类里面的操作即为封装,
封装可以为属性和方法添加私有权限
继承:子类默认继承父类所有的属性和方法
子类可以重写父类的属性和方法
多态:带入不同的对象,产生不同的结果,多态是指一类实物的多种形态,,一个抽象类有多个子类,多态依赖于继承
定义:多态是一种使用对象的方式,子类重写父类方法,调用不同的子类对象的相同父类方法,可以产生不同的执行结果
实现步骤:
定义父类,并提供公共方法
定义子类,并重写父类方法
传递子类对象给调用者,可以看到不同子类执行的效果不同
'''
# class dog():
#     def work(self):
#         print('指哪打哪')
# class armydog(dog):
#     def work(self):
#         print('追击敌人')
# class drugdog(dog):
#     def work(self):
#         print('追查毒品')
# class person():
#     def work_with_dog(self,dog):
#         dog.work()
#
# ad=armydog()
# dd=drugdog()
# xiaom=person()
# xiaom.work_with_dog(ad)
# xiaom.work_with_dog(dd)
'''
类属性和实例属性
类属性就是类对象所拥有的所有属性,它被该类的所有实例对象所共有
类属性可以使用类对象或者实例对象访问
记录某项数据始终保持一致,则定义类属性
类属性比实例属性更加节省空间
'''
# class Dog():
#     tooth=10
# wangcai=Dog()
# xiaohei=Dog()
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)
'''
类属性只能通过类对象修改,不能通过实例对象修改,如果通过实例对象修改类属性,表示创建了一个实例属性
'''
# class Dog():
#     tooth=10
# wangcai=Dog()
# xiaohei=Dog()
# Dog.tooth=12#修改类属性
# print(Dog.tooth)
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)
# wangcai.tooth=20#不能通过实例对象修改,如果通过实例对象修改类属性,表示创建了一个实例属性
# print(Dog.tooth)
# print(xiaohei.tooth)
'''
类方法,需要用装饰器@classmethod来标识为类方法对于类方法,第一个参数必须是类对象,一般以cls作为第一个参数
当方法中需要使用类对象
'''
class Dog():
    __tooh=10
    @classmethod
    def get_tooth(cls):
        return cls.__tooh
wangcai=Dog()
result=wangcai.get_tooth()
print(result)
'''
静态方法 用@statimethod
'''