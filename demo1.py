"""
print("hello world!") #字符串
print(123456)  #整数
print(2.33)  #小数
print(()) #元组
print([])#数组
print({})#字典
print(True) #布尔值 
"""
#你好
"""
print("hhh",2333)
print("哈哈"+"嘻嘻")
print("哈哈"*100 )
print(1+234*34/3)
print((1+2)*99/2)


#变量
#赋值

name = "张三"  #把张三这个值赋值给了a这个变量
print(name)
"""


# a = float(input("输入"))
# b = float(input("输入"))
# print("输入的数据为：",a+b)
# #数据格式的转换
# print(type(2333))
# print(type(2.33))
# print(type("哈哈哈"))
# print(type(()))
# print(type([]))
# print(type({}))
# print(type(True))


# a = "aohf klafkljapadsf;f"
# print(len(a))


"""
练习：通过代码获取两段内容，并且计算它们的长度的和
"""

# a = input("请输入内容1：")
# b = input("请输入内容2：")
# print("两段内容长度的和：",len(a)+len(b))  




# 元组基础

#元组,下标：从0开始编号
a = (1,2,3,4,"哈哈哈哈","llalalal",True,False,"dasdaf",32423)


#切片
# print(a[6])
# print(a[0:4])#左闭右开（区间）
# print(a[9:])

#查找下标,如果有很多个下标的时候，那么会从左往右输出最近的一个
# print(a.index("llalalal"))
# print(a.count(1))


# #二维元组
# b = (a,"丽丽","楷楷")
# print(b[0][4])






# # 数组基础

# # 元组一旦写好后就不能修改，但是数组可以
# a = [1,2,3,4,"哈哈哈哈","llalalal",True,False,"dasdaf",32423]
# # a.append("ajklf")
# print(a)

# # 插入一个值
# a.insert(1,"fasdf")
# print(a)
# # a.index()
# a.count()

# # a.pop():类似于剪切的功能，
# b = a.pop(1)
# c = a.pop(2)
# print(b+c)


# a.clear():清空数组
# a.clear()
# print(a)

# # a.extend
# r = ["affadf",2432]
# a.extend(a)
# # print(a)



# a.remove 移走
# a.remove("哈哈哈哈")
# print(a)
# remove(1)=remove(True)
# remove(0)=remove(False)

# d = [1,0,True,False]
# e = d.count(d)
# d.remove(0)
# print(d)



# 下标超出范围=越界
# xx = [2,23,4,5,3]



"""
python的语法：
1、所有方法都是小括号结尾，比如 print(),len(),input()
2、所有元组、数组、字典取值都是用[],比如：a[3]
3、元组、数组、字典的定义分别用的是()[]{}
"""

# 字典的基础

"""
字典的特点：
1、字典中的值是没有顺序的
2、字典的结构必须是键值对的结构:key:value
3、字典的取值是通过key去取value
"""
# a = {"name":"张三",
#     "age":25,
#     "phone":"tvwgbh"
# }



# # 取值
# print(a["name"])
# # 新增
# a["high"] = "170cm"
# print(a)
# # 修改
# a["name"]="youngkiefan"
# print(a)

#常用的方法
# get:相当于取值
# b = a.get("name")
# print(b)
# # pop：
# b = a.pop("name")
# print(a)
# # update ：相当于修改
# a.update(name="zhangsan")
# print(a)


# 两个的区别
# print(a["name"])
# print(a.get("name"))
# 错了前者是none后者是报错





# # 数组和字典的通用删除
# del a["name"]
# print(a)

# del a[2]


"""
练习：获取用户输入的个人信息并且存储到字典中
个人信息包括姓名、年龄、性别
"""

a = input("请输入姓名：")
b = input("请输入年龄：")
c = input("请输入性别：")
d = {"name":a,
     "age":b,
     "sex":c
     }

print(d)