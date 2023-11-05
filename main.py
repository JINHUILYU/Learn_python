# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        left_count = mergeSort(left_half)
        right_count = mergeSort(right_half)

        # Merge both halves and count significant inversions
        i = j = k = count = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > 2 * right_half[j]:
                count += len(left_half) - i
                j += 1
            else:
                i += 1

        arr[:] = sorted(arr)
        return left_count + right_count + count

    return 0


# Example usage
arr = [1, 20, 6, 4, 5]
print(mergeSort(arr))  # Output: 3

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

# encode 将字符转换为字节
# decode 将字节转换为字符
# encode 和 decode 的默认编码为 utf-8
# encode 和 decode 的参数 errors 可以设置为 'ignore' 忽略错误
# encode 和 decode 的参数 errors 可以设置为 'replace' 替换错误
tmp = 'Python'
print(tmp.encode())  # b'Python'
print(tmp.encode().decode())  # Python


# List
Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(Weekday[0])  # Monday
# List 搜索
print(Weekday.index('Monday'))  # 0
# List 添加
Weekday.append('Saturday')
print(Weekday)  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# List 插入
Weekday.insert(0, 'Sunday')
print(Weekday)  # ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# List 删除
Weekday.remove('Sunday')
print(Weekday)  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


# Tuple
# Tuple 一旦初始化就不能修改
letters = ('a', 'b', 'c')
print(letters[0])  # a
print(letters[:])  # ('a', 'b', 'c')


# Set
# Set 无序，不重复
st = set('hello')
print(st)  # {'h', 'e', 'l', 'o'}
st.add('a')
print(st)  # {'a', 'h', 'e', 'l', 'o'}
st.remove('a')
print(st)  # {'h', 'e', 'l', 'o'}


# Dict
# Dict 无序，key 唯一
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # 1
print(d.get('a'))  # 1
print(d.keys())  # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
print('a' in d)  # True
d.pop('a')
print(d)  # {'b': 2, 'c': 3}


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))  # 120

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
