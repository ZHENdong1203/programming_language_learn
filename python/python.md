# Python
## 1. python 标识符
标识符可包含数字，字母和下划线，不可以使用数字开头。

以下划线开头有特殊意义。
* 单下划线开头代表不能直接访问的类属性，需要通过类提供的接口进行访问，如_foo。
* 双下划线开头表示类的私有成员，如__foo
* 双下划线开头和结尾代表python里特殊方法专用的标识，如__init__()表示类的构造函数。
## 2. 注释
单行注释，使用#。

多行注释，使用三引号。
## 3. python输出
`print()`函数默认换行，不换行需要增加end参数，`print(obj, end='')`
## 3. 变量类型
### 标准数据类型
* 数字
* 字符串
* 列表
* 元组
* 字典
### 数字
python支持四种数字类型。
* int 整型
* long 长整型，结尾使用L或l
* float 浮点型
* complex 复数，由实部和虚部组成，可以用a+bj或complex(a,b)表示。复数的实部和虚部都是浮点型。

一个int类型的数`num`，可以通过`oct(num),hex(num)和bin(num)`转换为八进制，十六进制和二进制字符串。想要去掉进制前缀，使用`oct(num)[2:]`。

`complex()`函数可以将复数字符串转化为复数，如`complex("1+2j")`，下面的函数可以将复数转化为极坐标：
```python
from cmath import phase
s= input()
# 计算r
print(abs(complex(s)))
# 计算φ
print(phase(complex(s)))
```

`pow()`函数，可用于幂计算和模计算
```python
pow(base, exp, mod=None)
```

### 字符串
字符串运算符
* `+` 字符串连接
* `*` 重复输出字符串
```python
    str='Hello'
    print(str * 2)

=> 'HelloHello'
```
* `[]` 通过索引获取字符串中的字符，索引从0开始
* `[:]` 截取字符串的一部分，左闭右开
* `in` 成员运算符
格式化字符串,f-string
```python
num = 3.14159
print(f"{num:.2f}")

=> 3.14
```

字符串函数
* `split()` 其中`split(' ')`只把一个空格字符当作分隔符。多个连续空格会被视为“空内容”。 
* `strip(), lstrip(), rstrip()`
* `isupper()`和`islower()` 判断是否为大小写
* `upper()`和`lower()` 转换为大写或小写
* `join()` 把一个列表（或可迭代对象）中的元素用指定的分隔符连接成一个字符串。
```python
'分隔符'.join(可迭代对象)
```

### 列表
列表的数据项不需要有相同的类型，使用中括号。

操作符
* `+` 组合
* `*` 重复
* `in` 元素是否存在于列表中
* `for x in list: print(x)` 遍历
* `[]` 通过索引访问列表元素，左边索引从0开始，右边索引从-1开始
* `[:]` 切片，左闭右开
`[::-1]`倒序切片

列表方法
```python
    list.append()
    list.count()
    list.extend()
    list.insert(index,obj)
    list.index()
    list.pop()
    list.remove()
    list.reverse()
    list.sort()
```

`sort()`排序函数配合lambda表达式使用，可自定义按照哪个元素进行排序，sort默认升序，使用参数reverse=True可以改为降序，例如：
```python
# 列表list中的元素为[('a',2),('b',3),('b',2)]
# 先使用数字进行降序排列，再使用字母按照字母表顺序（升序）排列
result = [('a',2),('b',3),('b',2)]
result.sort(key=lambda x: (-x[1], x[0]))
print(result)

=> [('b', 3), ('a', 2), ('b', 2)]
```

生成字符串的排列
```python
from itertools import permutations
print list(permutations('abc',3))

=> [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
生成字符串的组合

如果输入是有序的，输出的组合也是有序的。
```python
from itertools import combinations 
print(list(combinations('12345',2)))

=> [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
```
有放回的组合

允许重复
```python
from itertools import combinations_with_replacement
print(list(combinations_with_replacement('12345',2)))

=> [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
```

### 元组
元组和列表类似，不要求元素的类型一致，但是元组不允许修改，同时使用小括号。

`namedtuple()`不需要整数索引来访问元组元素
```pyhton
from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print(xyz)
print(xyz.Class)

=> Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
=> Y
```
### 字典
字典是键值对，使用大括号。
其中字典的键唯一，并且不可变，所以键要使用数字，字符串或元组。

`defaultdict` 在插入时不需要检查key是否存在。`from collections import defaultdict
` 

`OrderedDict` 输出时可以保留键插入的循序`from collections import OrderedDict`

## 4. python运算符
算术运算符`+, -, *, /, %, **, //(向下取整)`

比较运算符`==, !=, >, <, >=, <=`

逻辑运算符`and, or, not`

成员运算符`in, not in`

身份运算符`is, not is`判断两个标识符是不是引用自一个对象
```python
a = 20
b = 20

if (a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

=> a 和 b 有相同的标识  
=> a 和 b 没有相同的标识   
```
## 5. python 条件语句
if-else
```python
if 判断条件：
    执行语句……
else：
    执行语句……
```
条件表达式（三元表达式）
```python
结果 = 表达式1 if 条件 else 表达式2
```

## 6. python循环语句
while循环
```python
while 判断条件(condition)：
    执行语句(statements)……
```
while-else，在循环条件为false时执行else语句块。
```python
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
```

for循环
```python
for iterating_var in sequence:
   statements(s)
```
for-else,else中的语句会在循环正常执行完后执行
```python
for num in range(10,20):  # 迭代 10 到 20 (不包含) 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)

10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数
```
`break`跳出整个循环

`continue`跳出当前循环，开始下一次循环

`pass`不做任何事情，用于占位

### 7. python函数
定义函数
```python
def functionname( parameters ):
   """函数文档"""
   function_suite
   return [expression]
```
函数的参数
* 必备参数
* 关键字参数
* 默认参数
* 不定长参数
```python
# 必备参数
def printme(str):
   "打印任何传入的字符串"
   print str
   return
 
#调用printme函数
printme()

# 关键字参数
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )

# 默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# 不定长参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
```

匿名函数，python使用lambda创建匿名函数
```python
lambda [arg1 [,arg2,.....argn]]:expression
```
```python
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
```
### 8. python文件
打开文件
```python
open(file, mode='r')
```
mode默认文本模式，r是读，w是写，a是追加，加b是二进制模式，加+是读写。r和w指针在开始，a指针在结尾。

方法
* close()
* write() 不会在字符串结尾加`\n`
* read() 
* tell() 返回文件内的当前位置，即下次读写会发生在文件开头多少字节之后
* seek(offset [,from]) offset表示要移动的字节数，from指定开始移动字节的参考位置。from是0，将文件开头作为移动字节的参考位置。是1，将当前位置作为参考位置。是2，将文件结尾作为参考位置。

### 9. python异常处理
except可以写特定的异常类型，也可以不写，else是当try执行没有发生异常时，才会执行。
```python
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
```
finally是无论是否发生异常，都会执行。
```python
try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
finally:
    如果没有异常执行这块代码
```
### 10. python面向对象
类定义
```python
class ClassName:
   """类的帮助信息"""   #类文档字符串
   class_suite  #类体
```
类的方法与普通函数有一个区别，必须有额外的第一个参数self。self代表类的实例，代表当前对象的地址。

内置类属性
* `__dict__` 类的属性，包含一个字典，由该类的数据属性组成
* `__doc__` 类的文档字符串
* `__name__` 类名
* `__moudle__` 类定义所在的模块
* `__bases__` 类的所有父类构成元素，包含了由所有父类组成的元组。

类的继承
```python
class 派生类名(基类名)
    ...
```
方法重写，如果父类方法的功能不能满足需求，可以在子类中重写父类的方法。

基础重载方法
* `__init__` 构造函数
* `__del__` 析构方法，删除一个对象
* `__str__` toString
* `__cmp__` 对象比较
运算符重载

类属性
* `_foo` 单下划线开头表示的是protected类型的变量，只允许本身和子类访问。不能用于`from module import *`。
* `__foo` 双下划线开头表示private类型，只允许这个类本身访问。python不允许实例化的类访问私有数据，但可以通过类名来访问，即`obj._className__attrName`
```python
class Runoob:
    __site = "www.runoob.com"

runoob = Runoob()
print runoob._Runoob__site

=> www.runoob.com
```

### 11. python日历
输入年月日，输出星期几，返回的是索引，0是Monday
```python
daynum = calendar.weekday(year, month, day)

=> 2
```
输入星期索引，返回名字
```python
day_name = calendar.day_name[daynum]

=> Wednesday
```
### 12. python集合
set是无序的数据结构，使用大括号。

集合的操作
* `s.union(t)` s和t的并集
* `s.intersection(t)` s和t的交集
* `s.difference(t)` 在s但是不在t
* `s.symmetric_difference(t)` 在s中但是不在t，同时还包括在t中但是不在s。
* `s.issubset(t)` s是否是t的子集

双端队列

左右两端都可以进行插入和删除`from collections import deque`

`zip()`函数
返回一个元组列表，第i个元组包含输入的序列或可迭代对象的第i个元素
```python
print(zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1]))

=> [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(zip(*X))

=> [(1, 6, 7), (2, 5, 8), (3, 4, 9)]
```

`eval()`函数会执行所有输入的python表达式

`any()` 迭代对象中有一个为True，any函数就返回True。

`all()`迭代对象中全部为True，all函数才返回True。

`groupby()`函数，对连续相同的元素进行分组，例如：
```python
from itertools import groupby

data = 'aaabbbccaaa'

for key, group in groupby(data):
    print(key, list(group))

=>
a ['a', 'a', 'a']
b ['b', 'b', 'b']
c ['c', 'c']
a ['a', 'a', 'a']
```

### 13. python HTML与XML
HTML解析需要重写handle函数
```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          if '\n' in data:
              print(">>> Multi-line Comment")
              print(data)
          else:
              print(">>> Single-line Comment")
              print(data)

    def handle_data(self, data):
        print(">>> Data")
        print(" " + data)

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("-> " + str(attr[0]) + " > " + str(attr[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag,attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("-> " + str(attr[0]) + " > " + str(attr[1]))

parser = MyHTMLParser()
number = int(input())
strList = ""
for i in range(number):
    strList += input()

parser.feed(strList)
```

xml解析为树结构
```python
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
```

### 14. python装饰器
用于在不修改函数或类定义的前提下，增加额外的功能。一个函数，增加另一个函数作为参数，并返回一个增强后的函数。
```python
def decorator(func):
    def wrapper():
        print("开始执行")
        func()
        print("执行结束")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
```
### 15. python numpy
Arrays

numpy数组接受一个list，并将其转化为一个numpy数组，list中所有元素的类型必须一致。第二个参数可以设置numpy数组元素的类型。
```python
import numpy

a = numpy.array([1,2,3,4,5])
print a[1]          

=> 2

b = numpy.array([1,2,3,4,5],float)
print b[1]          

=> 2.0
```

`arr.shape`可以输出当前数组`arr`的维度.

`arr.shape = (a,b)`可以将数组`arr`的维度设置为`a*b`.

`numpy.reshape(arr, (a,b))`可以将数组`arr`的维度设置为`a*b`。

`numpy.transpose(arr)`转置数组。

`arr.flatten()`将数组变化为一维。

`numpy.concatenate((array_1, array_2), axis = 1)` 拼接多个数组，axis参数默认是0，即按行拼接。为1是按列拼接。

零矩阵和一矩阵
`numpy.zeros((m,n))` 生成m行n列的零矩阵，`(m,n)`也可以作为元组传进去。可通过`dtype=float或int32`参数设置生成矩阵中元素的类型。

`numpy.ones((m,n))` 生成m行n列的一矩阵，`(m,n)`也可以作为元组传进去。

`numpy.identity(n)` 生成n行n列的单位矩阵，即对角线元素为1，其他元素为0。默认生成的元素为float类型。

`numpy.eye(m, n, k = 1)` 生成一个m行n列的矩阵，k=0就是单位矩阵，对角线元素为1，其他元素为0。k>0时，如果k=1，那么对角线的上一格斜线元素为1，其他元素为0.k=2即对角线上两格斜线元素为1。k<0时，即对角线下方。

numpy数组计算

可使用数学符号，也可以使用numpy的函数进行，以加法为例：
```python
import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)
print a + b                     

=> [  6.   8.  10.  12.]

print numpy.add(a, b)           

=> [  6.   8.  10.  12.]
```

`numpy.floor(arr)` 返回每个元素的下界。

`numpy.ceil(arr)` 返回每个元素的上界。

`numpy.rint(arr)` 返回每个元素四舍五入的整数。

`numpy.sum(arr, axis=0)` 数组按行求和。axis=1时，数组按列求和。默认axis=None，数组按所有维度求和。

`numpy.prod(arr, axis=0)` 数组按行求积。axis=1时，数组按列求积。默认axis=None,数组按所有维度求积。

`numpy.min(arr, axis=0)` 数组按行求最小值。axis=1时，数组按列求最小值。默认axis=None，数组按所有维度求最小值。

`numpy.max(arr, axis=0)` 数组按行求最大值。axis=1时，数组按列求最大值。默认axis=None，数组按所有维度求最大值。

`numpy.mean(arr, axis=0)` 数组按行求平均值。axis=1时，数组按列求平均值。默认axis=None，数组按所有维度求平均值。

`numpy.var(arr, axis=0)` 数组按行求方差。axis=1时，数组按列求方差。默认axis=None，数组按所有维度求方差。

`numpy.std(arr, axis=0)` 数组按行求标准差。axis=1时，数组按列求标准差。默认axis=None，数组按所有维度求标准差。

### 16. python 时间
将时间字符串转换为datetime格式,对应的格式代码为：

| 格式代码 | 含义                                | 示例                     |
|----------|-------------------------------------|--------------------------|
| `%a`     | 缩写的星期几                        | `Sun`                   |
| `%A`     | 全写的星期几                        | `Sunday`                |
| `%w`     | 星期几（0-6，0是周日）              | `0`                     |
| `%d`     | 日（01-31）                         | `05`                    |
| `%b`     | 缩写的月份                          | `May`                   |
| `%B`     | 全写的月份                          | `May`                   |
| `%m`     | 月（01-12）                         | `05`                    |
| `%y`     | 年的后两位（00-99）                 | `25`                    |
| `%Y`     | 年的完整四位                        | `2025`                  |
| `%H`     | 小时（24小时制，00-23）            | `13`                    |
| `%I`     | 小时（12小时制，01-12）            | `01`                    |
| `%p`     | AM或PM（大写）                      | `PM`                    |
| `%M`     | 分钟（00-59）                       | `09`                    |
| `%S`     | 秒（00-59）                         | `36`                    |
| `%f`     | 微秒（000000-999999）              | `000123`                |
| `%z`     | UTC偏移（±HHMM）                   | `+1000` / `-0700`       |
| `%Z`     | 时区名称（系统定义）               | `UTC`, `EST`（不推荐）  |
| `%j`     | 一年中的第几天（001-366）          | `123`                   |
| `%U`     | 一年中的第几周（周日为一周的开始） | `18`                    |
| `%W`     | 一年中的第几周（周一为一周的开始） | `19`                    |
| `%c`     | 本地日期和时间表示法                | `Tue Aug  5 23:00:00 2025` |
| `%x`     | 本地日期表示                        | `08/05/25`              |
| `%X`     | 本地时间表示                        | `23:00:00`              |

例如：
```python
t1 = "Sun 10 May 2015 13:54:36 -0700"
fmt = '%a %d %b %Y %H:%M:%S %z'
dt1 = datetime.strptime(t1, fmt)
```

