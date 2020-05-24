# 数据结构

## 准备

### 方法

leetcode：中文版，国际版

做题步骤：审题、思考多种解法并比较复杂度、写代码、测试用例

刷题方法：5分钟，看题解，重写，一天，一周

画脑图

**解题方法：if-else、for-while、recursion**

### IDE

Pycharm实用快捷键

- Ctrl + D  复制选定的区域或行
- Ctrl + Y    删除选定的行
- Ctrl + Numpad+/-   展开/折叠代码块（当前位置的：函数，注释等）
- Ctrl + Shift + F  或者连续2次敲击shift   全局查找
- Shift + F10    运行
- Shift + F9   调试
- Ctrl + Q    快速查看文档
- ALT+Enter，自动导入，自动创建，如函数
- Shift + Enter 换行

VS code

可以安装leetcode插件。

- Ctrl + Enter 换行
- shift + ctrl(command) + p，打开插件搜索栏

### code style

**使用自顶向下的编程模式**，将最重要的代码部分写在文件最上面，子函数放在下面。这样写的优点是代码的可读性强，且不易出错。

写代码时先定义高层次（主干）逻辑，后实现具体细节。

参考教程：[Clean Code: Book Review](https://markhneedham.com/blog/2008/09/15/clean-code-book-review/)

### 复杂度

常见时间复杂度：O(1)、O(logn)、O(n)、O(n^2)、O(2^n)、O(n!)

空间复杂度：与数组的长度或递归的深度有关。

递归，可以画出程序执行的状态树，通过主定理可以计算递归/分治的时间复杂度。

递归常用于二分查找、二叉树遍历、已排序的二维矩阵查找、归并排序。

## 数组、链表、跳表

### 线性表

一个线性表是某类元素的一个集合，还记录着元素之间的一种顺序关系。

线性表（简称表）通常用作复杂数据结构的实现基础。

一个表中可以有零个或多个元素，序列中的每个元素在表中有着确定的位置，称为该元素的下标，下标通常从0开始。

一个表中包含元素的个数称为表的长度，空表不含任何元素，长度为0。

当前结点的前后结点分别称为前驱节点与后继结点。在非空表中，存在着唯一的头元素与尾元素，除头元素外，每个元素有且仅有一个前驱元素；除尾元素外，每个元素有且仅有一个后继元素。

线性表的实现模型包括数组（顺序表）与链表。

### 数组 Array

Python中数组元素支持泛型，申请数组时，计算机底层开辟内存连续的地址，每一个地址直接通过内存管理器进行访问。 可以随机访问任何一个地址。

元素间的顺序关系由存储顺序表示。元素的下标是其逻辑地址，因此**数组的优点是元素访问操作的时间复杂度为O(1)，缺点是插入与删除操作的时间复杂度为O(n)**。

由于表元素的大小可能不等，因此对应于元素内置的顺序表，出现了元素外置的顺序表，顺序表的单元位置保存相应元素的引用信息（链接，索引）。其中元素外置的分离式顺序表结构便于动态扩容，因此也称为动态顺序表。

线性表的一个重要性质是可以插入与删除元素，因此对表的长度提出要求。因此对于不变的顺序表，可以在建表时根据确定的个数分配内存，如Python的tuple对象；对于可变的表，需要**区分表中当前元素个数与元素存储区的容量**。

顺序表的完整信息包括两部分，表中元素的集合与记录表中元素个数与容量的表信息。

**Python中的list与tuple就采用了顺序表的实现技术**，其中list就是采用分离式技术实现的动态顺序表，以达到如下要求：

- 基于下标的访问操作时间复杂度为O(1)，因此需要采用连续表设计；
- 允许任意加入元素，而且在元素的加入过程中，表对象的标识不变，因此需要采用分离式实现技术。

Python的官方系统中，list采用了如下实现策略以实现尾部插入元素的平均时间复杂度为O(1)。

- 建立空表时，系统分配能容纳8个元素的存储区；
- 执行插入操作时，如果元素区满就换一块四倍大的存储区；
- 如果当时的表已经很大（5000）时，换存储区容量加倍。

Python实现顺序表的主要代码如下所示。

```python
class Array(object):
    """顺序表"""
    def __init__(self, size=10):
        self.max = size  # 最大容量
        self.num = 0  # 当前长度
        self.data = [None] * self.max  # 初始化

    def is_empty(self):
        return self.num == 0

    def is_full(self):
        return self.num == self.max

    def len(self):
        return self.num

    def prepend(self, elem):
        """头插法"""
        if self.is_full():
            print('List is full')
            return False

        # 数组的群移操作
        for i in range(self.num, 0, -1):
            self.data[i] = self.data[i - 1]
        self.data[0] = elem
        self.num += 1
        return True

    def append(self, elem):
        """尾插法"""
        if self.is_full():
            print('List is full')
            return False
        
        self.data[self.num] = elem
        self.num += 1
        return True

    def insert(self, i, elem):
        """中间插入"""
        if i < 0 or i > self.num:
            print('Out of index')
            return False
        elif i == self.num:  # 尾插法
            self.data[self.num] = elem
        else:
            # 数组的群移操作
            for j in range(self.num, i, -1):
                self.data[j] = self.data[j - 1]
            self.data[i] = elem
        
        self.num += 1
        return True
    
    def lookup(self, elem):
        """查询指定元素"""
        for i in range(self.num):
            if self.data[i] == elem:
                print('{} found'.format(elem))
                return True
        print('{} not found'.format(elem))
        return False

    def del_first(self):
        if self.is_empty():
            print('List is empty')
            return False
        
        # 数组的群移操作
        for i in range(self.num - 1):
            self.data[i] = self.data[i + 1]
        self.num -= 1
        return True

    def del_last(self):
        if self.is_empty():
            print('List is empty')
            return False
        
        self.num -= 1
        return True

    def del_mid(self, i):
        if i < 0 or i >= self.num:
            print('Out of index')
            return False

        # 数组的群移操作
        for j in range(i, self.num - 1):
            self.data[j] = self.data[j + 1]
        self.num -= 1
        return True
    
    def show(self):
        for i in range(self.num):
            print(self.data[i], end='\t')
        print()

    def destroy(self):
        self.__init__()
```

### 单链表 Linked List

实现线性表的另一种方式是基于链接结构，用链接关系显式表示元素之间的顺序关系。基于链接技术实现的线性表称为链接表或链表。基本思想如下所示。

- 将表中的元素分别存储在一批独立的存储块（称为表的结点Node）中；
- 保证从组成表结构的任一结点可以找到与之相关的下一个结点；
- 在前一结点中用链接的方式显式记录与下一结点的关联。

实现链表有多种方式，其中单链表是在每个表结点中记录存储下一表元素的结点的标识（引用/链接）。

因此**单链表的结点是一个二元组（elem与next）**，元素域保存作为表元素的数据项（或数据项的关联信息），链接域保存同一个表里下一结点的标识。

**要确定一个单链表，只需要用一个变量保存这个表的头结点（第一个结点）的标识（引用/链接），这个变量称为表头变量或表头指针**。

对于尾结点，使用系统常量None作为链接域，即使用空链接表示链表的结束。如果一个表头指针的值是空链接，表明该表是空表。

对于单链表，扫描、定位或遍历（完整的扫描）操作的时间复杂度都是O(n)。

链表的删除与插入结点操作不会引起整个链表的群移操作，也不需要复制元素，因此时间复杂度为O(1)。

```python
class LinkListUnderFLow(ValueError):
    """自定义异常类"""
    pass

class LNode(object):
    """单链表结点"""
    def __init__(self, elem, next_=None):  # next_避免与标准函数next重名
        self.elem = elem
        self.next = next_

class LList(object):
    """单链表"""
    def __init__(self):
        self._head = None  # 头结点初始化

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        p = self._head  # 扫描指针
        while p is not None:  # 移动到尾结点，尾结点执行循环体代码
            p = p.next
            count += 1
        return count

    def prepend(self, elem):
        """头插法，适用于空链表，缺点是逆序"""
        # 上面一行等价于下面三行，但不建议使用
        # self._head = LNode(elem, self._head)

        q = LNode(elem)
        q.next = self._head
        self._head = q

    def append(self, elem):
        """尾插法"""
        p = self._head
        q = LNode(elem)  # 新结点

        if p is None:  # 空链表
            self._head = q
            return True

        while p.next is not None:  # 移动到尾结点，尾结点不执行循环体代码
            p = p.next
        p.next = q
        return True

    def insert(self, i, elem):
        """中间插入"""
        lens = self.length()
        if i < 0 or i > lens:
            print('Out of index')
            return False
        
        if i == 0:
            self.prepend(elem)
        elif i == lens:
            self.append(elem)
        else:
            p = self._head
            q = LNode(elem)
            j = 0

            while p.next is not None and j < (i - 1):  # 查找要插入的前一个结点p
                p = p.next
                j += 1
            q.next = p.next
            p.next = q

            return True

    def remove_elem(self, elem):
        """删除指定元素的结点，因为既需要找到指定元素的位置，还需要记住前一个元素的位置，因此需要两个指针"""
        p = self._head
        q = None  # 前一个结点

        while p is not None:
            if p.elem == elem:  # 已找到
                if p == self._head:  # 删除头结点，q = None
                    self._head = p.next
                else:
                    q.next = p.next
                break
            else:
                q = p
                p = p.next

    def remove_index(self, i):
        """删除指定位置的结点并返回该结点的值，删除结点时，头结点都需要单独考虑"""
        lens = self.length()
        if i < 0 or i >= lens:
            raise LinkListUnderFLow('Out of index')
        elif i == 0:
            e = self._head.elem
            self._head = self._head.next
        else:
            p = self._head
            j = 0
            while p.next is not None and j < (i - 1):  # 查找要删除的前一个结点p
                j += 1
                p = p.next
            q = p.next  # 要删除的结点
            e = q.elem
            p.next = q.next
        return e

    def pop_first(self):
        """删除单链表的头结点，并返回头结点的数据"""
        p = self._head

        if p is None:
            raise LinkListUnderFLow('Empty list')
        e = p.elem

        self._head = p.next
        return e

    def pop_last(self):
        """删除单链表的尾结点，并返回尾结点的数据"""
        p = self._head

        if p is None:
            raise LinkListUnderFLow('Empty list')
        elif p.next is None:
            e = p.elem
            self._head = None
        else:
            while p.next.next is not None:
                p = p.next
            e = p.next.elem
            p.next = None
        return e

    def show(self):
        p = self._head
        while p is not None:
            if p.next is not None:
                print(p.elem, end='\t')
            else:  # 最后一个结点后不需要制表符
                print(p.elem)
            p = p.next
```

### 循环链表

- 单循环链表简称循环链表，将终结点的指针端由空指针改为指向头结点，形成首尾相连的环形单链表。
- 循环链表与单链表的主要差异体现在判断空链表的条件（循环结束的控制）：rear == rear->next（只有头结点）。
- **不用头指针，而是用指向尾结点的尾指针来表示循环链表，这时查找头结点和尾结点的时间复杂度都是O(1)**。如用于线性表的拼接。

```python
class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LCList(object):
    def __init__(self):
        self._rear = None  # 保存尾指针

    def is_empty(self):
        return self._rear is None
    
    def length(self):
        if self._rear is None:  # 空链表
            return 0

        count = 0
        p = self._rear.next  # 头结点
        while p is not self._rear:
            p = p.next
            count += 1
        count += 1  # 尾结点未计数
        return count

    def prepend(self, elem):
        """头插法，不适用于空链表，缺点是逆序"""
        q = LNode(elem)

        if self._rear is None:
            self._rear = q
            self._rear.next = q
        else:
            q.next = self._rear.next
            self._rear.next = q

    def append(self, elem):
        """尾插法，同样不适用于空链表"""
        # q = LNode(elem)
        # q.next = self._rear.next
        # self._rear.next = q
        # self._rear = q
        
        # 尾插法等价于头插法+更新尾结点
        self.prepend(elem) 
        self._rear = self._rear.next

    def insert(self, i, elem):
        """中间插入"""
        lens = self.length()
        if i < 0 or i > lens:  
            raise LinkListUnderFLow('Out of index')
        
        if i == 0:
            self.prepend(elem)
        elif i == lens:
            self.append(elem)  # 尾指针需要移动
        else:
            p = self._rear.next
            q = LNode(elem)
            j = 0
            while p.next is not None and j < (i - 1):
                p = p.next
                j += 1
            q.next = p.next
            p.next = q

    def remove_elem(self, elem):
        """删除指定元素的结点，因为既需要找到指定元素的位置，还需要记住前一个元素的位置，因此需要两个指针"""
        p = self._rear.next
        q = None

        while p != self._rear:
            if p.elem == elem:
                if q is None:
                    self._rear.next = p.next
                else:
                    q.next = p.next
                break
            else:
                q = p
                p = p.next
        
        if p.elem == elem:
            q.next = self._rear.next
            self._rear = q

    def remove_index(self, i):
        """删除指定位置的结点并返回该结点的值，删除结点时，头结点都需要单独考虑"""
        lens = self.length()
        if i < 0 or i >= lens:
            raise LinkListUnderFLow('Out of index')
        elif i == 0:  # 删除头结点
            q = self._rear.next
            e = q.elem
            self._rear.next = q.next
        else:
            p = self._rear.next
            j = 0
            while p.next != self._rear and j < (i - 1):
                p = p.next
                j += 1
            q = p.next
            e = q.elem
            p.next = q.next
            if i == (lens - 1):  # 删除尾结点
                self._rear = p
        return e

    def pop_first(self):
        """删除单链表的头结点，并返回头结点的数据"""
        if self._rear is None:
            raise LinkListUnderFLow('Empty list')

        p = self._rear.next
        self._rear.next = p.next
        e = p.elem
        return e

    def pop_last(self):
        """删除单链表的尾结点，并返回尾结点的数据"""
        if self._rear is None:
            raise LinkListUnderFLow('Empty list')
        
        e = self._rear.elem
        p = self._rear
        while p.next != self._rear:
            p = p.next
        p.next = self._rear.next
        self._rear = p
        return e

    def show(self):
        p = self._rear.next
        while p != self._rear:
            print(p.elem, end='\t')
            p = p.next
        print(p.elem)
```

### 双向链表

- 要求支持反向移动，因此需要双向循环链表。前驱结点用于反向移动，后继结点用于正向移动。
- 同时定义头指针与尾指针，对于双向链表，两端的插入与删除操作都能高效完成。从任一结点出发，访问前后的相邻结点都是O(1)操作。
- 结点结构包括前驱结点prior与后继结点next，注意插入与删除操作的顺序；
- 插入与删除不定位置元素的操作时，均需要分三种可能性，即头结点、尾结点、中间结点；
- JAVA中的单链表是双向链表。双向链表在工程中可用于实现LRU。

```python
class DLNode(object):
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next = next_

class DLList(object):
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None
    
    def length(self):
        count = 0
        p = self._head
        while p is not None:
            p = p.next
            count += 1
        return count

    def prepend(self, elem):
        """头插法，不适用于空链表，缺点是逆序"""
        p = self._head
        q = DLNode(elem)

        if p is None:  # 空链表
            self._rear = q
        else:
            q.next = p
            p.prev = q
        self._head = q

    def append(self, elem):
        """尾插法，同样不适用于空链表"""
        p = self._rear
        q = DLNode(elem)

        if p is None:
            self._head = q
        else:
            p.next = q
            q.prev = p
        self._rear = q

    def insert(self, i, elem):
        """中间插入"""
        lens = self.length()
        if i < 0 or i > lens:
            raise LinkListUnderFLow('Out of index')

        p = self._head
        q = DLNode(elem)
        if i == 0:
            q.next = p
            p.prev = q
            self._head = q
        elif i == lens:
            p = self._rear
            p.next = q
            q.prev = p
            self._rear = q
        else:
            j = 0
            while p.next is not None and j < (i - 1):
                p = p.next
                j += 1

            p.next.pre = q
            q.next = p.next
            q.prev = p
            p.next = q

    def remove_elem(self, elem):
        """删除指定元素的结点，因为既需要找到指定元素的位置，还需要记住前一个元素的位置，因此需要两个指针
        使用索引删除时即对于remove_index函数，由于有索引，因此可以直接使用数字作为指针
        """
        p = self._head
        q = None

        while p is not None:
            if p.elem == elem:
                if q is None:  # 删除头结点
                    self._head = p.next
                elif p.next is None:  # 删除尾结点
                    q.next = None
                    self._rear = q
                else:
                    p.next.prev = q
                    q.next = p.next
                break
            q = p
            p = p.next

    def remove_index(self, i):
        """删除指定位置的结点并返回该结点的值，删除结点时，头结点都需要单独考虑"""
        lens = self.length()
        if i < 0 or i >= lens:
            raise LinkListUnderFLow('Out of index')
        elif i == 0:
            p = self._head
            e = p.elem
            self._head = p.next
        elif i == (lens - 1):
            p = self._rear
            e = p.elem
            p.prev.next = None
            self._rear = p.prev
        else:
            p = self._head
            j = 0
            while p.next is not None and j < (i - 1):
                p = p.next
                j += 1
            q = p.next
            e = q.elem
            
            q.next.prev = p
            p.next = q.next
        return e

    def pop_first(self):
        """删除单链表的头结点，并返回头结点的数据"""
        p = self._head

        if p is None:
            raise LinkListUnderFLow('Empty list')

        e = p.elem
        self._head = p.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        """删除单链表的尾结点，并返回尾结点的数据"""
        if self._head is None:
            raise LinkListUnderFLow('Empty list')

        p = self._rear
        e = p.elem
        p.prev.next = None
        self._rear = p.prev
        return e

    def show(self):
        p = self._head
        while p is not None:
            if p.next is not None:
                print(p.elem, end='\t')
            else:
                print(p.elem)
            p = p.next
```

### 跳表 Skip List

链表查询操作的时间复杂度为O(n)，对其进行优化。如当链表元素有序时，可以使用二分查找。

**跳表的前提条件时元素有序，对标平衡树与二分查找**，是一种插入/删除/搜索的时间复杂度都是O(logn)的数据结构。

优点是原理简单、容易实现、方便拓展、效率更高。因此在一些热门的项目中用来替代平衡树，如Redis、LevelDB。

跳表的实现方式是添加一级索引，同理也可以继续添加二级索引，先查询索引后查询原始链表。

缺点是在增加、删除结点时，需要更新索引，因此维护成本高，时间复杂度增大至O(logn)。

跳表的空间复杂度为O(n)。

因此**为加速查询，跳表的实现基于升维思想与空间换时间**。



### 应用：约瑟夫问题



### 应用：魔术师发牌问题



### 实战：数组

#### [移动零](https://leetcode-cn.com/problems/move-zeroes/)

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

1. 暴力解法

将所有零元素移动到数组的末尾。时间复杂度O(n^2)。

```python
from typing import List

class Solution(object):
    def move_zeroes(self, nums: List[int]) -> None:
        """暴力解法，所有零元素移动到数组的末尾"""
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            else:  # 遇到零元素则与下一个非零元素交换
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
```

2. 双指针法局部优化

转换思路，将所有非零元素移动到数组的末尾。时间复杂度O(n)。

快指针用于记录当前要判断的元素，慢指针用于记录当前非零元素的个数，即下一个非零元素的位置。

第一次遍历将非零元素赋值到左边，第二次遍历将非零元素右边的元素置为零。

```python
class Solution(object):
    def move_zeroes_1(self, nums: List[int]) -> None:
        """双指针法，一维数组的坐标变换，所有非零元素移动到数组的末尾"""
        i = 0  # 记录下一个非零元素的位置
        for j in range(len(nums)):
            if nums[j] != 0:
                # 如果不为0，向前覆盖，数据不会丢失
                nums[i] = nums[j]  
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0
```

3. 继续优化

对于所有（除最后一个）前导零的数组：[0，0，0，…，0，1]来说，双指针法中的第二次遍历多余，因此继续优化。

注意慢指针之前的所有元素都是非零的，当前指针即快指针与慢指针之间的元素都是零。

以此为依据，遇到非零元素时，将慢指针与快指针的数据交换，可以使用一次遍历替代二次遍历。

```python
class Solution(object):
    def move_zeroes_2(self, nums: List[int]) -> None:
        """最优解法，将慢指针与快指针的数据交换，可以使用一次遍历替代二次遍历"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                # 进行交换或直接赋值，原因是索引为i-j之间的元素都是0
                # nums[i], nums[j] = nums[j], nums[i]
                if i != j:
                    nums[i] = nums[j]
                    nums[j] = 0
                i += 1
```

#### [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

首先明确面积等于底边宽度与短板高度的乘积。

1. 暴力解法

遍历数组，嵌套循环，时间复杂度O(n^2)。

两层循环，只需要满足下标`i<j`即可。

```python
class Solution(object):
    def resarea(self, height: List[int]) -> None:
        """暴力解法，两层循环"""
        res = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(res, area)
        return res
```

2. 双指针法

双指针代表的是**可以作为容器边界的所有位置的范围**。

重难点在于理解双指针法的正确性。

- 定义规则为，从左右边界向中间收敛，原因是在左右边界时底边宽度最大，移动时如果短边高度变大，面积有可能增大；
- 每次移动短板，可以消去一部分状态的面积，如当`height[i]<height[j]`时，将状态`S(i, j)`移动到`S(i+1, j)`，相当于消去`S(i, j-1)、S(i, j-2)..S(i, i+1)`状态集合。原因是对于消去的状态集合，短边高度小于等于`S(i, j)`，底边宽度小于`S(i, j)`，因此面积小于等于`S(i, j)`；
- **双指针法的核心思想在于每一次移动，意味着排除掉一根柱子**。如将状态`S(i, j)`移动到`S(i+1, j)`，相当于排除掉将`i`柱子与任何一次柱子的组合，即排除掉`i`柱子。因此无论柱子`i`与`j`哪根更长，都可以删掉一行或一列的搜索空间。经过 *n* 步以后，就能排除所有的搜索空间，检查完所有的可能性。也就是说，**双指针法的本质是缩减搜索空间**。搜索空间的减小过程如下面动图所示：

![search-space-shrink](https://pic.leetcode-cn.com/48fa92510ccbc963d7e49da6a2d7302ebf42233345522a42df435df18bc42fa4.gif)

```python
class Solution(object):
    def max_area_1(self, height: List[int]) -> None:
        """双指针法，左右边界向中间收敛，一层循环"""
        res = 0
        i = 0
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)
            if height[i] < height[j]:  # 移动短板
                i += 1
            else:
                j -= 1

        return res
```

3. 继续优化

取消min()函数的调用，原因是已经比较了`height[i]`与`height[j]`的相对大小。

尽管改动很小，但执行用时下降较明显。

```python
class Solution(object):
    def max_area_2(self, height: List[int]) -> None:
        """双指针法优化"""
        res = 0
        i = 0
        j = len(height) - 1

        while i < j:
            if height[i] < height[j]:  # 移动短板
                area = (j - i) * height[i]
                res = max(res, area)
                i += 1
            else:
                area = (j - i) * height[j]
                res = max(res, area)
                j -= 1

        return res
```

#### [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

由于n的取值无法确定，因此无法直接使用暴力解法。建议没有思路时考虑**数学归纳法**。

在此基础上进行泛化，泛化的思想是提取**最近重复子问题，如回溯、递归、分治、动态规划都是基于思想**。

本质就是求斐波那契数列，有多种解法，如递归、循环。

- 递归时如果不加缓存，如新建数组，否则性能会很低；
- 循环时不需要新建数组，只需要设置最后三个值，向前累加即可，不需要将中间变量全部保存。

1. 暴力解法（递归）

直接使用递推公式进行实现。

```python
class Solution(object):
    def climb_stairs(self, n: int) -> int:
        """暴力解法，直接递归，也可使用尾递归"""
        if n <= 2:
            return n
        
        for i in range(3, n + 1):
            return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)
```

2. 动态规划

保存中间结果，以空间换时间。

```python
class Solution(object):
    def climb_stairs_1(self, n: int) -> int:
        """动态规划"""
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

3. 循环

经验证，**循环的执行用时小于递归，大于动态规划**。说明循环体中的语句很耗时，即使只是简单的赋值操作。

```python
class Solution(object):
    def climb_stairs_2(self, n: int) -> int:
        """使用循环求取斐波那契数列"""
        if n <= 2:
            return n
  
        f1 = 1
        f2 = 2
        f3 = 0  
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        
        return f3
```

#### [两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

1. 暴力解法

两层循环，时间复杂度O(n^2)。注意不能排序，原因是索引位置就变了。

```python
class Solution(object):
    def two_sums(self, nums: List[int], target: int) -> List[int]:
        """"暴力解法"""
        for i in range(len(nums) - 1):
            # for j in range(len(nums)):  有重复，已计算过
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

2. 两遍哈希表

为了优化时间复杂度，需要更高效的方法来检查数组中是否存在目标元素。如果存在，需要获取到它的索引。

**保持数组中每个元素与其索引相互对应的最好方法是哈希表**。

哈希表通过以空间换取时间的方式，将查找速度从O(n)降低到O(1)。也就是说，使用哈希表可以起到一层循环的作用。

分两步进行，先将数据put进哈希表，再从哈希表中get出指定元素的索引。

```python
class Solution(object):
    def two_sums_1(self, nums: List[int], target: int) -> List[int]:
        """两遍哈希表"""
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = i
        
        for i, value in enumerate(nums):
            temp = target - value
            j = hashmap.get(temp)
            if j is not None and i != j:
                return [i, j]
```

2. 一遍哈希表

将两步合为一步进行，同时进行put与get，即再插入数据之前，检查是否已存在当前元素所对应的目标元素。

但是实际上经验证，一遍哈希表的执行用时大于两边哈希表，原因是判断目前元素是否存在需要循环操作。

注意返回的数组是所求索引位置的逆序。

```python
class Solution(object):
    def two_sums_2(self, nums: List[int], target: int) -> List[int]:
        """一遍哈希表"""
        hashmap = {}
        for i, value in enumerate(nums):
            temp = target - value
            if temp in hashmap:  # 循环
                j = hashmap.get(temp)
                if i != j:
                    return [j, i]
            hashmap[value] = i
```

#### [三数之和](https://leetcode-cn.com/problems/3sum/)

两数之和的升级版。

1. 暴力解法

三重循环，**难点在于去重，首先进行排序**。

```python
class Solution(object):
    def three_sums(self, nums: List[int]) -> List[int]:
        """"暴力解法，三重循环，难点在于去重"""
        lens = len(nums)
        if lens < 3:
            return []

        nums.sort()  # 方便去重
        if nums[0] >= 0:
            return []

        res = []
        for i in range(lens - 2):
            for j in range(i + 1, lens - 1):
                for k in range(j + 1, lens):
                    if (nums[i] + nums[j] + nums[k] == 0) and ([nums[i], nums[j], nums[k]] not in res):
                        res.append([nums[i], nums[j], nums[k]])

        return res
```

2. 哈希表+两层循环

哈希表代表一层循环，未完成，程序有问题。

```python
class Solution(object):
    def three_sums_1(self, nums: List[int]) -> List[int]:
        """哈希表"""
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = i

        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                temp = (nums[i] + nums[j]) * (-1)
                if temp in hashmap and ([nums[i], nums[j], temp] not in res):
                    res.append([nums[i], nums[j], temp])

        return res
```

3. 双指针法，左右夹逼

双指针法在数组与链表中都很有用，**数组中双指针法通常有两种用法，快慢指针与左右指针，其中左右指针通常需要先排序**。

```python
class Solution(object):
    def three_sums_2(self, nums: List[int]) -> List[int]:
        """双指针法"""
        if len(nums) < 3:
            return []

        nums.sort()  # 排序的时间复杂度为O(nlogn)
        res = []

        for k in range(len(nums) -2):
            if nums[k] > 0: break  # j > i > k
            if k > 0 and nums[k] == nums[k - 1]: continue  # skip the same `nums[k]`

            i = k + 1  # 左指针
            j = len(nums) - 1  # 右指针
 
            while i < j:  # 左右夹逼
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1  # skip the same `nums[i]`                    
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1  # skip the same `nums[j]`
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1

        return res
```

#### [数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

1. 排序后查找

时间复杂度O(NlogN)，空间复杂度O(N)，Python语言中排序所用蒂姆排序算法空间复杂度为O(N)。

```python
class Solution(object):
    def find_repeat_number(self, nums: List[int]) -> int:
        """先排序"""
        nums.sort()
        temp = -1

        for num in nums:
            if num == temp:
                return num
            else:
                temp = num
```

2. 哈希表查找

时间复杂度O(N)，空间复杂度O(N)。

```python
class Solution(object):
    def find_repeat_number_1(self, nums: List[int]) -> int:
        """集合去重"""
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num
            else:
                nums_set.add(num)
```

3. 数组原地排序

时间复杂度O(N)，空间复杂度O(1)。

需要注意交换两数的表达式为：`nums[nums[i]], nums[i] = nums[i], nums[nums[i]]`，而非`nums[i], nums[nums[i]] = nums[nums[i]], nums[i]`。

原因是`a, b = c, d` 的原理是先暂存元组 `(c, d)` ，然后“按顺序“赋值给 `a` 和 `b` 。如果 `nums[i]` 先被赋值， `nums[nums[i]]` 指向的元素就变了。

```python
class Solution(object):
    def find_repeat_number_2(self, nums: List[int]) -> int:
        """原地交换"""
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == i:  # 假设数组中不存在重复元素，则满足该条件
                i += 1  # 比较下一位
                continue
            elif nums[i] == nums[nums[i]]:  # 同一个数字多次出现，因此重复
                return nums[i]
            else:
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]  # 超时
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # 原地交换
```

#### [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

给你两个有序整数数组 *nums1* 和 *nums2*，请你将 *nums2* 合并到 *nums1* 中*，*使 *nums1* 成为一个有序数组。

1. 合并后排序

时间复杂度为O((M+N)log(M+N))，原因是没有利用数组有序的条件。

```python
class Solution(object):
    """合并两个有序数组成为一个有序数组"""
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """合并后排序"""
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
```

2. 双指针法

**双指针从后往前移动**，时间复杂度O(M+N)，空间复杂度O(1)。

注意`nums1[:n] = nums2[:n]`不等于`nums1 = nums2`，[后者不满足指向不变的要求](https://leetcode-cn.com/problems/merge-sorted-array/solution/gelthin-gui-bing-pai-xu-by-gelthin/)。

```python
class Solution(object):
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """双指针法"""
        if 0 == m:  # 直接原地拷贝nums2，nums1 = nums2语句会修改了nums1的指向
            nums1[:n] = nums2[:n]
        elif 0 == n:  # 直接返回
            pass
        else:
            i = m - 1
            j = n - 1
            p = m + n - 1  # 当前位置
            
            while i >= 0 and j >= 0:
                if nums1[i] <= nums2[j]:  # nums1 的元素尽量少动
                    nums1[p] = nums2[j]
                    j -= 1
                    p -= 1
                else:
                    nums1[p] = nums1[i]
                    i -= 1
                    p -= 1                
            
            if j >= 0:  # 第二个数组的表头有剩余元素
                nums1[p - j: j + 1] = nums2[: j + 1]  # 必然有 p - j == 0，因为剩下的是最小的，必然是copy到最前面
```

### 实战：链表

#### [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

单链表反转。

1. 迭代

使用双指针（快慢指针），注意需要将cur.next的地址进行备份，否则就找不到了。**出错的原因不理解**。

每次将cur的next指向pre，然后将pre与cur前进一位。

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """单链表反转"""
    def reverse_list(self, head: ListNode) -> ListNode:
        """迭代解法"""
        cur = head
        pre = None

        while cur is not None:
            tmp = cur.next  # 备份原来cur节点的next地址
            cur.next = pre
            pre = cur
            cur = tmp

            # tmp = cur
            # tmp.next = pre
            # pre = cur
            # cur = cur.next
        
        return pre
```

2. 递归

**递归主要包括两部分：递归中进行的操作、递归结束的判断**。

假设在反转过程中，列表当前元素之后已反转，之前未反转，则需要将当前结点的next.next指向当前结点本身。

也就是说，在每次函数在返回的过程中，让当前结点的下一个结点的 next 指针指向当前节点。

```python
class Solution(object):
    def reverse_list_1(self, head: ListNode) -> ListNode:
        # head is None：空链表
        # head.next is None：到尾部
        if head is None or head.next is None: return head

        p = self.reverse_list_2(head.next)
        head.next.next = head
        head.next = None
        return p
```

#### [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

判断链表中是否有环，不需要返回环的位置。

1. 暴力解法

遍历，并申请内存（哈希表/集合）保存走过的结点，如果重复说明有环。

代码执行结果显示，时间复杂度较低，但空间复杂度较高。

```python
class Solution(object):
    def has_cycle(self, head: ListNode) -> bool:
        """暴力解法，申请内存，如哈希表"""
        hashmap = {}
        p = head

        while p is not None:
            if hashmap.get(p, None):
                return True
            else:
                hashmap[p] = 1
            p = p.next
        return False
```

2. 快慢指针

快慢指针相遇表明链表有环。

```python
class Solution(object):
    def has_cycle(self, head: ListNode) -> bool:
        """双指针法，快慢指针"""
        if head is None:  # 空链表
            return False

        fast = head.next
        slow = head

        while fast != slow:
            if (fast is None) or (fast.next is None):
                return False                           
            slow = slow.next
            fast = fast.next.next
        return True
```

#### [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

判断链表中是否有环，如果存在需要返回环的位置。



#### [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

1. 循环

**关于链表的问题，可以引入哑结点简化边界条件的处理**。

m、n分别为l两个链表的长度，合并操作的时间复杂度为O(m+n)，空间复杂度为O(1)。

设置头结点（哨兵结点），便于最终返回合并后的链表。维护prev结点，调整next指针。

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """合并两个有序链表"""
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """循环"""
        head = ListNode(-1)  # 新的头结点，哑结点
        prev = head  # 拷贝

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        # if l1 is not None:
        #     prev.next = l1
        # else:
        #     prev.next = l2
        prev.next = l1 or l2
        
        return head.next
```

2. 递归

**抽象出子问题，子问题与原问题具有相同的结构，因此考虑自上而下的递归**。

`合并(L1, L2)`，当`L1.val<L2.val`时等价于`L1.next = 合并(L1.next, L2)`。

也就是说，可以将原问题转化成两个链表头部值较小的一个节点与剩下元素的 `merge` 操作结果合并。

m、n分别为l两个链表的长度，合并操作的时间复杂度为O(m+n)，空间复杂度为O(m+n)，栈空间的大小取决于递归调用的深度。

```python
class Solution(object):
    def merge_two_lists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归"""
        if l1 is None:  # 边界条件
            return l2
        elif l2 is None:  # 边界条件
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_lists_1(l1.next, l2)
            return l1  # 返回值较小的结点
        else:
            l2.next = self.merge_two_lists_1(l2.next, l1)
            return l2
```

## 栈、队列、双端队列、优先队列

**容器结构中可以包含一组其他类型的数据对象，称之为元素，支持对这些元素的存储、管理与使用**。

栈与队列是两类最常用的容器，两者是使用最广泛的数据结构。

**栈与队列通常用于在计算过程中保存临时数据**，这些数据是在计算过程中发现或产生，在后面的计算中可能会用到。

如果数据项这样的存储机制在编程时就可以确定，设置几个变量进行临时存储即可。但如果需要存储的数据项不能事先确定，就需要采用更复杂的机制存储与管理，**这样的临时存储机制称为缓冲存储或缓存。栈与队列是使用最多的缓存**。

栈与队列是最简单的缓存结构，只支持数据项的存储与访问，保证元素存入与取出的顺序即可，不支持数据项之间的任何关系。

栈与队列的实现相对简单，原因是两者通常使用顺序表或链表实现，限制了规则意味着需要实现的方法减少。

具体实现系统接口，如插入、删除等操作。

### 栈 Stack

先进后出，添加删除操作的时间复杂度为O(1)，查询O(n)。

要求只在表尾进行删除和插入操作。表尾称为栈顶，表头称为栈底。**top指定栈顶**。

栈可用于如浏览器的后退，撤销、函数的实现、编译器检测代码中的括号匹配问题、数值的进制转换等。

基于栈结构的特点，在实际应用中，通常只会对栈执行以下两种操作：

- 向栈中添加元素，此过程被称为"进栈"（入栈或压栈）；
- 从栈中提取出指定元素，此过程被称为"出栈"（或弹栈）。

栈也分顺序存储结构与链式存储结构，分别简称顺序栈与链栈。通常使用顺序存储结构进行实现，Python中即列表。

栈有初始化容量。当栈满时进行扩容，未满时大小不变。因此栈中元素的个数通常不等于栈的最大容量。

使用数组实现时，int **top表示当前栈顶位于数组的第几号元素，用于索引数组**。当栈为空时，top=-1。

**push时，先赋值后移动top。pop时，先移动top后赋值。顺序并不绝对，与数组索引的取值有关**。

```python
class Stack(object):
    def __init__(self, size=10):
        self.max = size
        self.top = -1  # 空栈，top表示当前栈顶位于数组的第几号元素
        self.data = [None] * self.max

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.max - 1)

    def pop(self):
        if self.is_empty():
            raise StackUnderFLow('Stack empty')
        e = self.data[self.top]
        self.top -= 1
        return e

    def push(self, elem):
        if self.is_full():
            raise StackUnderFLow('Stack full')
        self.top += 1
        self.data[self.top] = elem

    def show(self):
        for i in range(self.top, -1, -1):
            print(self.data[i], end='\t')
        print()
```

### 队列 Queue

先进先出，添加删除操作的时间复杂度为O(1)，查询O(n)。

**栈常用顺序表实现，队列常用链表实现**。约定队尾插入，队头删除。

```python
class ListNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None
    
    def is_empty(self):
        return self.head is None

    def push(self, elem):
        q = ListNode(elem)

        if self.rear is None:
            self.rear = q
            self.head = q
        else:
            self.rear.next = q        
            self.rear = q

    def pop(self):
        if self.head is None:
            raise QueueUnderFLow('Queue empty')

        e = self.head.elem          
        self.head = self.head.next
        return e

    def show(self):
        p = self.head

        while True:
            print(p.elem, end='\t')
            if p == self.rear:
                break
            p = p.next
        print()
```

### 双端队列 Deque

Double End Queue，两端都可以进出的队列，添加删除操作的时间复杂度为O(1)，查询O(n)。



### 优先队列 Priority Queue

元素取出时的顺序不再是先进先出后先进后出，而是按照元素的优先级取出。

- 插入操作的时间复杂度为O(1)；
- 取出操作O(logN)，按照元素的优先级取出。

为实现有序，底层具体实现的数据结构较为多样与复杂， 如堆heap、二叉搜索树bst。



### 实战：栈

#### [括号匹配](https://leetcode-cn.com/problems/valid-parentheses/)

识别括号，开括号进栈，闭括号进行匹配。后进先出符合栈的特性。

**当问题具有最近相关性时可以使用栈解决**。

如果最终栈为空，说明字符串完全匹配。

暴力解法可以使用两重循环，将遇到的成对的括号用空字符串代替。

1. 栈 + 哈希表 + 生成器

```python
parens = '()[]{\}'
open_parens = '([{'
opposite = {')': '(', ']': '[', '}': '{'}

class Solution(object):
    def gene_parens(self, text: str):
        """括号生成器"""
        i = 0
        lens = len(text)

        while True:
            if i < lens and text[i] not in parens:
                i += 1
                continue
            if i >= lens:
                break
            yield text[i], i  # 返回括号以及括号所在的位置，位置信息用于生成出错信息
            i += 1

    def check_parens(self, s: Stack, text: str) -> bool:
        """括号匹配问题"""
        for pr, i in self.gene_parens(text):
            if pr in open_parens:   # 开括号进栈
                s.push(pr)
            else:  # 闭括号进行匹配
                oppo = opposite.get(pr)
                top = s.pop()
                if oppo != top:  # 不匹配
                    print(oppo, top)
                    print('Unmatch is found at {}, for {}'.format(pr, i))
                    return False
        
        print('All match')
        return True
```

2. 栈 + 哈希表

```python
class Solution(object):
    def is_valid(self, s: str) -> bool:
        """使用哈希表（字典）"""
        # parens = '()[]{\}'
        # open_parens = '([{'
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []  # 顺序栈 

        for c in s:
            # if c in open_parens: stack.append(c)
            if c in dic.values(): stack.append(c)
            elif len(stack) == 0 or dic.get(c) != stack.pop(): return False  # ']'
        return len(stack) == 0  # '['
```

3. 栈

不使用哈希表，而是使用条件语句进行配对的校验。

但执行结果显示空间复杂度没有下降。

```python
class Solution(object):
    def is_valid_1(self, s: str) -> bool:
        """不使用哈希表（字典），手写对应关系"""
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or c != stack.pop(): 
                return False

        return len(stack) == 0
```

#### [最小栈](https://leetcode-cn.com/problems/min-stack/)

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

注意与优先队列有区别，原因是要求在在常数时间内检索到最小元素，而不是要求每次取出时返回最小元素。因此本质上还是栈。

使用两个栈实现，一个维护出入的关系，一个维护最小元素的栈。

题目要求的每个操作的时间复杂度为O(1)，每个操作最多调用两次栈操作。体现以空间换时间的思想。

1. 两个栈的元素不一一对应（辅助栈和数据栈不同步）

push时，如果当前元素大于最小栈的栈顶元素，则最小栈不变。缺点是每次push与pop时都需要进行比较，优点是节省内存。

```python
import math

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        if x <= self.min_stack[-1]:  # 最小值有可能出现多次，如0、1、0
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
           self.min_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
```

2. 两个栈的元素一一对应（辅助栈和数据栈同步）

**辅助栈中保存每个元素对应的最小值**。在任意时刻，栈内元素的最小值存储在辅助栈的栈顶元素中。

push时调用内置函数min()进行比较，将最小值压入栈中，pop时不需要进行比较，直接弹出即可。

```python
class MinStack(object):
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        x = self.stack.pop()
        self.min_stack.pop()
```

#### 使用栈实现队列

使用两个栈。



#### [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

两柱子之间矩形的高度取决于最矮的柱子。因此**本质上是求每根柱子对应的最长的连续的底边长度**。对于当前柱子，要求底边连续表明左右柱子的高度小于当前柱子。

1. 暴力解法

代码有误。

```python
class Solution(object):
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """暴力解法，三重循环"""
        if len(heights) == 0:
            return 0
        else:
            max_area = heights[0]

        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = heights[i]
                for k in range(i + 1, j + 1):  # 查找左右边界中的最小高度
                    min_height = min(heights[k], min_height)
                area = min_height * (j - i + 1)
                print(min_height, i, j)
                max_area = max(max_area, area)
        return max_area
```

2. 双指针法

枚举以每根柱子为高度的最大矩形的面积。找到每根柱子的左右边界是第一次出现的比它矮的柱子。

```python
class Solution(object):
    def largest_rectangle_area_1(self, heights: List[int]) -> int:
        """暴力解法，双指针，两重循环，超时"""
        max_area = 0
        n = len(heights)

        for i in range(n):  # 每根柱子的左右边界是第一次出现的比它矮的柱子
            left = i
            right = i
            cur_height = heights[i]
            while left > 0 and heights[left] >= cur_height: left -= 1  # heights = [2,1,5,6,2,3] -> left = 0
            while right < n and heights[right] >= cur_height: right += 1  # heights = [2,1,5,6,2,3] -> right = 6
            area = cur_height * (right - left - 1)
            max_area = max(area, max_area)

        return max_area
```

3. 栈

双指针法有重复。

缓存数据时，从左向右缓存，计算结果的顺序是从右向左，并且计算完成后就不再需要，符合后进先出的特性。因此，**选用栈作为缓存的数据结构**。栈中存储下标。**有序的栈可以O(1)知道左边界的位置**。

计算最大宽度时，没有使用遍历，而是使用了栈内存放的下标信息。因此，计算最大宽度的时间复杂度为O(1)。

- 新元素大于栈顶元素时，表明栈内全部元素的右边界未知；
- 新元素小于等于栈顶元素时，表明该新元素是栈内部分元素的右边界。

-1

哨兵

单调栈

```python
class Solution(object):
    def largest_rectangle_area_2(self, heights: List[int]) -> int:
        """栈"""
        stack = [-1]
        max_area = 0
        n = len(heights)

        for i in range(n):  # 单调栈
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                area = heights[stack.pop()] * (i - stack[-1] - 1)  # 任何一个栈内元素的左边界都是栈顶下一个元素的下标
                max_area = max(area, max_area)
            stack.append(i)  # 单调栈，右边界未知
        
        while stack[-1] != -1:  # 非空栈
            area = heights[stack.pop()] * (n - stack[-1] - 1)  # 任何一个栈内元素的左边界都是栈顶下一个元素的下标
            max_area = max(area, max_area)
        
        return max_area
```

### 实战：队列

#### 使用队列实现栈

使用两个队列。



#### [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

滑动窗口相关的问题可以使用队列解决。

双端队列。



