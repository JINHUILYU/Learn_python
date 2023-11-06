**注意事项**
* 以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import *` 而导入
* 以双下划线开头的 `__foo` 代表类的私有成员
* 以双下划线开头和结尾的 `__foo__` 代表 Python 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数

**print**

* print() 默认输出是换行的，如果要实现不换行需要加上end参数

**运算**

* 整除运算 x // y 结果为整数
* 除法运算 x / y 结果为浮点数
* 乘方运算 x ** y 结果为x^y^

**String**

```python
# 字符串
s = 'Python'
# 切片
print(s[0:2])  # Py
print(s[2:])  # thon
print(s[:])  # Python
print(s[::2])  # Pto
print(s[::-1])  # nohtyP
print(s[-3:-1])  # ho
# 替换
print(s.replace('P', 'p'))  # python
# 查找
print(s.find('y'))  # 1
# 转大小写, upper()、lower()、swapcase()、capitalize()、istitle()、isupper()、islower()
# 去空格,strip()、lstrip()、rstrip()
# 格式化
print('hello %s' % 'world')  # hello world
print('hello {}'.format('world'))  # hello world
s = ['2017', '03', '29', '22:00']
print('-'.join(s))  # '2017-03-29-22:00'
print(('-'.join(s)).split('-'))  # ['2017', '03', '29', '22:00']
```

**字符串编码**

所有的 Python 字符串都是 Unicode 字符串，当需要将文件保存到外设或进行网络传输时，就要进行编码转换，将字符转换为字节，以提高效率。

```python
# encode 将字符转换为字节
# decode 将字节转换为字符
# encode 和 decode 的默认编码为 utf-8
# encode 和 decode 的参数 errors 可以设置为 'ignore' 忽略错误
# encode 和 decode 的参数 errors 可以设置为 'replace' 替换错误
tmp = 'Python'
print(tmp.encode())  # b'Python'
print(tmp.encode().decode())  # Python
```

**可以在while语句中添加判断逻辑**

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('count >= 5')
```

**range()**

* start: 从start开始
* end: 在end前结束，不包括end
* scan: 间距，默认为

**模块**

一个py文件就是一个模块，通过import语句导入，一个模块只会被导入一次。

**from ... import ...**

模块提供了类似名字空间的限制，允许 Python 从模块中导入指定的符号（变量、函数、类等）到当前模块。导入后，这些符号就可以直接使用，而不需要前缀模块名。

```python
import hello
hello.sayhello()

from hello import sayhello
sayhello()

from hello import *  # 导入模块内的所有函数
```

**container**

容器(container)可以包含其他任意对象，容器主要包括序列和映射两类。序列的每个元素都有自己的编号，而映射每个元素则有一个叫做“键”的名字。

