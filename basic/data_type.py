# 整数的十六进制用法：以0x为前缀、0-9、a-f表示
i = 0xff
print(i)
print(15*16**1+15*16**0)
print("-------------")
# 浮点数（之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的）
# 1.23x109和12.3x108是完全相等的,0.000012可以写成1.2e-5
# 存在四舍五入误差
f = 1.2e-2
print(f)
print(1.2e-5 == 0.12e-4)
print("-------------")
# 字符串
print("I'm OK")
# 转义字符用法
print("\"I'm OK\"")
print("---\n换行\n---")
print("---\\---")
print("\taa\tbbb\tcccc")
# 不使用转移字符时
print(r'\n\\\n\\\n')
# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
# 多行字符串
print('''A
B
C''')
print(r"""ABC\n
abc""")
print("-------------")
# 布尔值
print(True and False) # 与
print(1+1 and 2+0)
print(1<1 and 2>2)
print(True or False) # 或：只要一个为真，结果就为真
print(not True) # 非
print("-------------")
# 空值 None
print(None)
print("-------------")
# 变量（变量名必须是大小写英文、数字和_的组合，且不能用数字开头）
a = 1
print(a)
a = "a"
print(a)
# 这种变量本身类型不固定的语言称之为动态语言（Python），与之对应的是静态语言（Java）
# 变量在计算机内存中的表示
# 如：a = "ABC"
# python解释器: 1.在内存中创建了一个‘ABC’的字符串 2.内存中创建了一个名为a的变量，并把它指向'ABC'
# 也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
print("-------------")
# 常量
PI = 3.14159265359
print("用全部大写的变量名表示常量只是一个习惯上的用法")
# 除法：1./（结果为浮点数）2.//（地板除，结果为整数）
print(10/3)
print(9/3)
print(10//3)
print(10%3) #取余
# 无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的
# 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。