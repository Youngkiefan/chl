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


#元组,下标：从0开始编号
a = (1,2,3,4,"哈哈哈哈","llalalal",True,False,"dasdaf",32423)


#切片
print(a[6])
print(a[0:4])#左闭右开（区间）
print(a[9:])

#查找下标,如果有很多个下标的时候，那么会从左往右输出最近的一个
# print(a.index("llalalal"))
# print(a.count(1))


# #二维元组
# b = (a,"丽丽","楷楷")
# print(b[0][4])
