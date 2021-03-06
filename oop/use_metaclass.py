# 元组：动态创建类
# 先定义metaclass，就可以创建类，最后创建实例
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 通过元组（ListMetaclass.__new__()）创建类
class MyList(list, metaclass=ListMetaclass):
    pass
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。


L = MyList()
L.add(1)
print(L)
