### Python 二叉堆实现

Python中**heapq模块基于列表实现了最小堆排序算法**。其中heap表示堆，q表示队列queue。

参考教程[Python 的 heapq 模块源码分析](https://mp.weixin.qq.com/s?__biz=MzUyOTk2MTcwNg==&mid=2247485256&idx=1&sn=224fe196324fee819b15b24b194d7f1b&chksm=fa5840cdcd2fc9db9dc88e4039c1d1e83af4147ba312140441517961474c4dacca8abd260e0c&mpshare=1&scene=1&srcid=0531mvABm9QT3L3boFEuDEhF&sharer_sharetime=1590893031296&sharer_shareid=98a5c34fd80e29d03560a4baaa3a1d4b&key=fcbd74047a90d9d311890422cc9fd664a5b9528465bb186b02abed28645622feb0e4743235a13e046a8aafbf89df72af734b9e851b21dc7aefdf570cddc8c1b20deea1b8b7e6b8a6d4841e1af0c752e4&ascene=1&uin=MjAyMjAzOTYxOQ%3D%3D&devicetype=Windows+10+x64&version=62090070&lang=zh_CN&exportkey=AYvxfWYxHDb0%2FjkIBU%2FKB2I%3D&pass_ticket=%2FuHphQmXcE1V%2BFsoQyPRpPI8PfMsDUev%2FRqSyOl9USInXUTF%2FW%2FVhKp%2FdiDBpvEj)手动实现最小堆。

二叉堆最基本的函数包括：

- `heappush()`：向堆中添加元素；
- `heappop()`：从堆中弹出元素；
- `heapify()`：让列表具备堆特征。

下面的伪代码是这三个函数的内部逻辑。

```python
def heappush(heap, item):
    """先在堆数组的尾部添加，再上浮到正确位置"""
    # 1. 在堆数组的尾部添加新结点
    # 2. 将该结点进行上浮操作，移动到正确位置 -> _siftup()
    # 具体操作是与父结点进行比较，如果小于父结点，则与父结点进行交换，并重复该过程，
    # 边界条件是根结点，也就是说新添加的元素在当前堆中是最小值
    
def heappop(heap):
    """先将堆数组尾部的元素移动到堆顶，再下沉到正确位置"""
    # 1. 弹出堆顶的元素，堆顶空缺，然后将堆数组尾部的元素移动到堆顶
    # 2. 将新的堆顶元素进行下沉操作，移动到正确位置 -> _siftdown()
    # 具体操作是与两个子结点进行比较，如果小于两者的最小值，则表明当前位置就是正确的位置
    # 如果大于两者的最小值，则将当前结点与较小的子结点进行交换，并重复该过程，
    # 边界条件是叶子结点，也就是达到堆数组的尾部

def heapify(data):
    """将无序序列（如列表）转换成堆，原地转换 in-place"""
    # 1. 从最后一个非叶子节点 (n // 2) 到根节点为止，进行下沉 -> _siftdown()
    # 逆序下沉的目的是通过尽可能少的移动操作将列表转换成合法的堆，也就是满足堆特征
```

从伪代码中可以抽象出上浮或下沉操作，分别封装为`_siftup()`与`_siftdown()`函数。这两个函数是内部函数，无法通过import导入。

```python
def _siftup(heap, startpos, pos):
    """"startpos表示，如果是新增元素，startpos=0"""
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) // 2
        parent = heap[parentpos]
        if parent > newitem:  # 要求父结点小于子结点
            heap[pos] = parent
            pos = parentpos
            continue
        else:
            break
    heap[pos] = newitem
 
def _siftdown(heap, pos):
    """pos表示要下沉的元素下标"""
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    while pos < endpos:
        # Bubble up the smaller child until hitting a leaf.
        lchild = 2 * pos + 1  # 当前索引结点的左右孩子的索引
        rchild = 2 * pos + 2
        if lchild >= endpos:  # 如果lchild是叶子结点，说明已经到底，退出循环
            break
        childpos = lchild  # 假设要交换的是左孩子，接下来进行比较，原因是当前结点要与较小的子结点进行交换
        # print(heap[childpos], heap[rchild], heap[pos])
        if rchild < endpos and heap[childpos] > heap[rchild]:
            childpos = rchild
        if heap[childpos] > heap[pos]:  # 如果当前结点比子结点都小，则退出循环
            break
        heap[pos], heap[childpos] = heap[childpos], heap[pos]  # 交换
        # print('pos={}, heap[pos]={}, childpos={}, heap[childpos]={}'
            # .format(pos, heap[pos], childpos, heap[childpos]))
        # heap[pos] = heap[childpos]  # 局部优化
        pos = childpos  # 下一层
```

关于`_siftdowm()`函数，优化部分的部分代码没看明白，优化前是每次比较都进行交换，优化后减少了交换的次数。后续继续看吧。

```python
def _siftdown(heap, pos):
    """pos表示要下沉的元素下标"""
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    while pos < endpos:
        # Bubble up the smaller child until hitting a leaf.
        lchild = 2 * pos + 1  # 当前索引结点的左右孩子的索引
        rchild = 2 * pos + 2
        if lchild >= endpos:  # 如果lchild是叶子结点，说明已经到底，退出循环
            break
        childpos = lchild  # 假设要交换的是左孩子，接下来进行比较，原因是当前结点要与较小的子结点进行交换
        print(heap[childpos], heap[rchild], heap[pos])
        if rchild < endpos and heap[childpos] > heap[rchild]:
            childpos = rchild
        # if heap[childpos] > heap[pos]:  # 如果当前结点比子结点都小，则退出循环
        #     break
        # heap[pos], heap[childpos] = heap[childpos], heap[pos]  # 交换
        print('pos={}, heap[pos]={}, childpos={}, heap[childpos]={}'
            .format(pos, heap[pos], childpos, heap[childpos]))
        heap[pos] = heap[childpos]  # 局部优化
        pos = childpos  # 下一层
        print('heap={}'.format(heap))
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftup(heap, startpos, pos)
```

需要注意的是heapq模块中函数的命名方法有所不同，`_siftup()`与`_siftdown()`函数的功能相反，由于在heapq模块中将二叉堆索引减小称为下沉，反之称为上浮。

