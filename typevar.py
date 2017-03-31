#coding=utf-8 #代码中有中文,即使是包含在注释里面的,就会出错.所以加上中文注释很重要

'''
交换变量
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738264643de15c5c4abad47dd9510e3b86286acb8000
'''
a = 'ABC'
b = a 
a = 'XYZ'
print b
#ABC
print a
#XYZ

'''
逻辑运算
and、or和not与、或、非
'''
print True and True
print True or False
print not True

# 全部大写的变量名表示常量只是一个习惯
import math
print math.pi

# 数做除法还是取余数，结果永远是整数.整数运算结果永远是精确的。
print 10 % 3  #1
print 10 / 3  #3
print 10.0 / 3  #3.33333333333

