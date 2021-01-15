# Python

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [python基础](#python基础)
- [Python内置函数](#python内置函数)
- [Python的数据结构](#python的数据结构)

<!-- /code_chunk_output -->

## python基础
- 取整运算 
    ```python {cmd=true}
    # 9 / 4 = 2.5
    # 9 // 4 = 2 // 只取整数,不四舍五入
    # 9 // -4 = -3 //带有负数的取整会向下取整
    #-9 // 4 = -3
    print('%d//%d=%d' % (9, 4, 9 // 4))
    print('%d//%d=%d,%d//%d=%d' % (-9, 4, -9 // 4, 9, -4, 9 // -4))
    ```
    ```kotlin {cmd=true}
    //  9/-4=-2
    // -9/4=-2
    fun main(args:Array<String>){
        System.out.print("9/-4=${(9/-4).toString()},-9/4=${(-9/4).toString()}")
    }
    ```
- 带有负数的取余运算
    ```python {cmd=true}
    # 9 % 4 = 1
    # 9 % -4 = -3 // 余数 = 被除数 - 除数 * 商 --> 9 - (-4 * -3) = 9-12 = -3 
    # 此处的商得依据取整运算的商
    # -9 % 4 = 3 // -9 - (4 * -3) = -9+12 = 3
    print('%d%%%d=%d' % (9, 4, 9 % 4))
    print('%d%%%d=%d,%d%%%d=%d' % (-9, 4, -9 % 4, 9, -4, 9 % -4))
    ```
    ```kotlin {cmd=true}
    //9  % -4 = 1
    //-9 % 4  = -1
    fun main(args:Array<String>){
        System.out.print("9%-4=${9%-4},-9%4=${-9%4}")
    }
    ```
- 幂运算
    ```python {cmd=true}
    print("%d**%d=%d" % (2,3,2**3)) # 2**3=8
    ```
- 赋值
    ```python {cmd=true}
    a = b = c = 20 # 链式赋值
    d,e,f = 30,40,50 #系列解包赋值
    d,f = f,d # 用解包赋值进行值交换
    print(id(a),id(b),id(c),d,e,f)
    ```
- 比较运算
    ```python {cmd=true}
    a = [1,2,3,4]
    b = [1,2,3,4]
    # a == b --> true //值相同
    # a is b --> flase //对象不同
    print(a==b,a is b)
    ```
- bool函数,python所有对象都有内置bool值,(False,0,None,空字符串,空列表,空元组,空字典,空集合为False)
    ```python {cmd=true}
    print(bool(''),bool({}),bool(0),bool(None),bool(-1),bool(' '),bool(1),bool('123'))

    a = 0

    if a: # 可以简化判断
        print('true')
    else:
        print('false')
    ```
- if-else的一种写法
    ```python {cmd=true}
    print('true-left' if 1 > 0 else 'right-flase')
    print('true-left' if 1 == 0 else 'right-flase')
    ```
- else可以和while、for循环搭配使用
- String是一种不可变序列,其本身可以进行序列操作而无需进行转化
    - 查找：`s.index(s)` `s.find(s)` `s.rindex(s)` `s.rfind(s)` 区别在于r是最后一次出现的位置，find未找到不会报错而是返回-1,注意，找到位置返回的都是正向索引
    - 大小写转换：`upper()`转大写 `lower()`转小写 `swapcase()` 所有大小写反转 `capitalize()` 第一个字母大写，其余小写 `title()`所有单词第一个字母大写，其余小写
    - 对齐操作: `center()`居中对齐，第一个参数指定宽度，即字符长度，第二个参数指定填充符，省略时将填充空格; `ljust()` `rjust()` 左对齐右对齐,参数同`center()`; `zfill()`右对齐，只能指定宽度，左边由`0`填充, `zfill()`会跳过首位的`-`字符，但依然计算在字符长度中; 这四个函数若指定宽度小于字符串，则返回字符串本身
        ```python {cmd=true}
        print('str is str'.center(30,'?'),'-99.1'.rjust(8,'0'), '-99.1'.zfill(8), '-???'.zfill(8))
        # ??????????str is str?????????? 000-99.1 -00099.1 -0000???
        ```
    - 分隔: `split()` `rsplit()` 返回一个列表,`sep`参数未分隔字符,默认为空格,`maxsplit`为最大分割次数,进行分割最多`maxsplit`次,剩下未分割部分会作为整体返回到列表的元素中,`rsplit()`从右往左分，但是返回的列表依然是正序排列
        ```python {cmd=true}
        print('1 2 3 4 5 6'.rsplit(maxsplit=3)) # ['1 2 3', '4', '5', '6']
        ```
    - 判断：(为什么我不用统一的正则？)
        - `isidentifier()` 是否是合法的标识符,即由字母数字下划线组成,且首字母不能为数字
            ```python {cmd=true}
            print('1a_a1'.isidentifier(),'a_a1'.isidentifier(),'这也能算作字母'.isidentifier())
            ```
        - `isspace()` 是否全部由空白字符组成,空白字符包括回车,换行,水平制表符
        - `isalpha()` 是否全部由字母组成
        - `isdecimal()` 是否全由十进制数字组成(不包括汉字数字罗马数字等)
        - `isnumeric()` 是否全由数字组成(包括汉字数字罗马数字等)
        - `isalnum()` 是否全由数字和字母组成
    - `replace` 替换
    - `join` 将序列中的字符串合并成一个字符串,由拼接符调用,如果传入字符串，则字符串会被当做序列
        ```python {cmd=true}
        print('*'.join('python'),''.join(('p','y','t','h','o','n'))) # p*y*t*h*o*n python
        ```
    - 格式化：
        - %占位符：`%s%s`% (s1,s2), `%s`字符串 `%i` `%d`整数 `%f` 浮点数, `%10.3f`10表示该字符要占10个宽度左边用空格补充，.3表示保留三位小数
        - {}占位符: `{0},{1},{0}`.format(s0,s1), 只有一个占位符{}可省略, `{0:10.3}`中10表示宽度,.3表示三位数(小数点不占位置), `{0:.3f}`.3f表示三位小数
        - f: f'{变量1},{变量2}'
    - 指定编码: `s.encode(encoding='GBK')` 对应的解码 `byte.decode(encoding='utf-8')` 编码解码格式需相同
- 函数：
    - python可以使用默认值参数,相应的也可以使用关键字参数,即传参时指定参数名称传值;参数如果不定,即个数可变的位置参数,使用`*参数名`的方式,方法内参数是一个元组;如果关键字形参的个数不定时,使用`**参数名`,方法内参数是一个字典;如果参时既有个数可变的位置参数,也有个数可变的关键字形参时,个数可变的位置形参需要在关键字形参前面;当传值时，也可以使用`*序列`的方式传值给位置参数;如果使用字典当作参数传入个数可变的位置形参中，则需要使用`**字典`的方法且元素个数需要对应
    - python的函数不需要显示声明返回值，当函数返回多个值时，其结果为元组
    - `global`可以将函数内的局部变量转为全局变量,`global`必须在函数内声明,如果在函数内使用全局变量，也要使用`global`,否则使用的时函数内同名的局部变量
        ```python {cmd=true}
        a = 1

        def add():
            a = 2
            print('add()',a) # add() 2

        add()
        print(a) # 1
        ```
- 异常: 使用`tyr:  except BaseException as e:  else:  finally:`  except和else择一执行;也可以`import traceback` 然后调用`traceback.print_exc()`自行输入错误信息
- 类：
    - 类也是poython的对象
        ```python {cmd=true}
        class Test:
            pass
        print(type(Test), id(Test), Test) # <class 'type'> 2621300176096 <class '__main__.Test'>
        print(type(Test()), id(Test()), Test()) 
        # <class '__main__.Test'> 1996688392096 <__main__.Test object at 0x000001D0E3E6FFA0>
        ```
    - 类中的实例方法的调用除了可以用对象调用外,还可以用`类名.方法()`然后传入对象的方式调用,这是默认参数`self`的作用
    - 类属性,即类中方法外的变量,其值被所有类的对象所共享,**类的对象**的类属性都指向**类对象**的类属性地址
    - 类方法,需要使用`@classmethod`声明,有默认参数且参数名一般为`cls`,调用时使用`类名.类方法()`不需要传参,一般用来修改类属性
    - 静态方法需要使用`@staticmethod`方法声明
    - 类的对象可以动态绑定属性和方法,直接将类的对象当作`dict`赋值即可
    - 表示私有需要在属性或者方法前加`__`,但仍可以用`dir`取获取真正内部属性或者方法来访问带`__`的
    - python支持多继承,且多继承按照广度优先(python3),如果使用了父类的属性或者方法，会从多继承父类从左往右的顺序依次寻找,并逐层向上,可以使用`类名.__bases__`查看父类,使用`类名.__mro__`查看继承的结构
    - python的多态有动态语言的特性，即虽无继承关系，但有这样的方法，依然可以传入并调用
        ```python {cmd=true}
        class Duck:
            def walk(self):
                print('duck walk')
            def swim(self):
                print('duck swim')

        class Bird:
            def walk(self):
                print('this one walk like a duck')
            def swim(self):
                print('this one swim like a duck')
        # 动态语言的特性,只有具有这两个方法,即可传参调用
        def fly(duck):
            duck.walk()
            duck.swim()
        
        fly(Duck()) # duck walk // duck swim
        fly(Bird()) # this one walk like a duck // this one swim like a duck
        ```
    - `__add()__`:`+`操作符重载, `__len()__`：`len`函数重载, `__new__`方法会先于`__init__`方法执行
        ```python {cmd=true}
        class Test:
            def __init__(self):
                print('init id={}'.format(id(self)))

            def __new__(cls,*args,**kwargs):
                print('__new__ cls id={}'.format(id(cls)))
                res = super().__new__(cls)
                print('super __new__ res id={}'.format(id(res)))
                return res

        print('cls id={}'.format(id(Test)))
        print('instance id={}'.format(id(Test())))
        # cls id=1391585087232
        # __new__ cls id=1391585087232
        # super __new__ res id=1391591890512
        # init id=1391591890512
        # instance id=1391591890512
        ```
    - 深拷贝：使用copy模块的`deepcopy`函数
## Python内置函数

- `bool`: 返回对象的bool值
- `type`: 返回对象的类型
- `del`: 删除对对象的引用,可用来删除字典中元素
- `zip`: 将多个可迭代对象对应打包成元组,然后返回整个元组的对象(python3),对应的可以使用`*+zip对象`来还原
- `tuple`: 创建元组对象
- `dict` : 创建字典对象
- `list` : 创建列表
- `set` : 创建集合,如传入的是可迭代对象,会将其转换成集合,而不是将对象当作集合的元素
- `ord` : 获取字符原始值
- `char` : 获取获取原始值对应的字符
- `dir` : 查看类的属性和方法列表
- `len` : 获取内容长度
##  Python的数据结构

- 列表：`[val1,val2,val3]`,`list([val1,val2,val3])`,也可以使用列表生成式生成,python的列表不受类型的限制,无需存储同一类型,正向索引0到N-1,逆向索引-N到-1,对list切片步长为负数时,会以从后往前的顺序
    ```python {cmd=true}
    lst = [0,1,2,3,4,5,6,7]
    lst = [i for i in range(0,8)]
    print(lst[5:1:-2]) # [5, 3]
    print(lst[::-1]) # [7, 6, 5, 4, 3, 2, 1, 0]

    lst.sort(reverse=True) # 对象直接排序
    lst=sorted(lst) # 会返回排序后的新对象
    print(lst)

    lst2 = ['a','b','c']
    lst[3:] = lst2
    print(lst) # [0, 1, 2, 'a', 'b', 'c'] 将lst2追加到lst[3:]切片的结果中
    lst.append(lst2) 
    print(lst) # [0, 1, 2, 'a', 'b', 'c', ['a', 'b', 'c']]
    lst.pop()
    print(lst) # [0, 1, 2, 'a', 'b', 'c']
    lst.extend(lst2)
    print(lst) # [0, 1, 2, 'a', 'b', 'c', 'a', 'b', 'c']
    ```
- 字典：`{key=value,key2=value2}`,`dic(key=value,key2=value2)`,删除元素使用`del`
    - 使用字典生成式生成字典
        ```python {cmd=true}
        dic = {key:value for key,value in zip(['key1','key2'],['value1','value2','value3','value1'])}
        print(dic) # {'key1': 'value1', 'key2': 'value2'}
        del dic['key1']
        dic['key1'] = 100
        print(dic) # {'key2': 'value2', 'key1': 100}
        ```
- 元组：是不可变序列,`(value,value2,value3)`(这种方式赋值()可以省略 ),`tuple((value,value2,value3))`,只有一个元素的元组需要添加`,`即`(value1,)`,不可变序列不可增删,其元素也是不可变的时也无法更改,在多任务环境下不需要加锁
- 集合：是没有value的字典,因此其是无序的,且值是不重复的,`{value1,value2,value3}`,`set(range(6))`,`set([1,2,3,4,5,6,6,7,7])`==>`{1,2,3,4,5,6,7}`,也可以用集合生成式生成,空集合只能用`set()`,而不能用`{}`,因为这是空字典,`issubset`判断是否是另一个集合的子集,`issuperset`判断是否是另一个集合的超集,`isdisjoint`判断是否有交集
    ```python {cmd=true}
    s = {1,2,3,4}
    s.add(5)
    s.update((6,7,8))
    s.remove(8)
    s.discard(9)
    print(s) # {1, 2, 3, 4, 5, 6, 7}

    s2 = {3,4,5,6,"1"}
    print(s.intersection(s2),s & s2)  # 返回交集 {3, 4, 5, 6}

    print(s.union(s2),s | s2) # 返回并集 {1, 2, 3, 4, 5, 6, 7, '1'} 

    print(s.difference(s2),s-s2) # 返回差集(s去掉交集的部分) {1, 2, 7}

    print(s.symmetric_difference(s2),s ^ s2) # 返回对称差集(s,s2去掉交集的所有值的集合) {1, '1', 2, 7}

    s.pop() #随机删除一个元素,随机是hash的特性,实际上是选择并删除一个元素
    ```
- 对比：

|数据结构|是否可变|是否可重复|是否有序|定义符号|
| --- | --- | --- | --- | :---: |
|列表list|可变|可重复|有序|[]|
|字典dict|可变|key不可重复,value可重复|无序|{key:value}|
|元组tuple|不可变|可重复|有序|()|
|集合set|可变|不可重复|无序|{}|

## 上下文管理器
- 上下文管理器主要用于自动调用关闭方法，即使发生异常也会调用关闭方法
- 常用于打开文件，`open`函数返回的即是一个遵守上下文管理器协议的对象的实例
    ```python
    with open("","r") as file:
        pass
    ```
- 你也可以用自己的类来完成上下文协议，用于自动关闭资源，只需要实现`__enter__()`,`__exit__()`两个方法
    ```python
    class Auto(object):
        def __enter__(self):
            pass
        def __exit__(self):
            pass
    with Auto() as a:
        pass
    ```
## os包

### 常用属性
- `name`: 返回操作系统的名称字符，windows只会返回`nt`，可以使用`getpass`模块的`getpass.getuser()`来获取当前用户名字符
- `curdir`: 就是`.`
- `pardir`: 就是`..`
- `sep`:  分隔符`\\`，应该是根据系统自动选择
- `extsep`: 文件拓展名分隔符
- `linesep`: 换行符

### 常用函数
- `system(str)`: 在win下可以看作cmd命令
- `startfile(path)`: 启动文件，填写可执行文件路径即可直接执行
- `getcwd()`: 返回当前工作目录
- `listdir(path)`: 返回指定路径下的文件和目录信息
- `mkdir(path[,mode])`: 创建目录
- `mkdirs(path[,mode])`: 创建多级目录
- `rename(path[,mode],path[,mode])`: 更改文件
- `rmdir(path)`: 删除目录
- `removedirs(path)`: 删除多级目录
- `chdir(path)`: 设置path为工作路径
- `walk(path)`: 遍历文件目录及其子目录，返回一个walk对象

### path模块
- `abspath(paht)`: 用于获取文件或者目录的绝对路径
- `exists(path)`: 判断文件是否存在
- `join(path, name)`: 拼接目录与目录或者目录与文件路径
- `splitext()`: 分类文件名和拓展名
- `basename(path)`: 从一个路径中提取文件名
- `dirname(path)`: 从一个路径中提取路径
- `isDir(path)`: 判断是否为dir