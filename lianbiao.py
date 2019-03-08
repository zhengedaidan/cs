class Node:
    def __init__(self,data,next=None):
        self.item = data
        self.next = next

class SingleLinkList:
    def __init__(self,head=None):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def lenth(self):
        count = 0
        cur = self.__head  # 头节点不能丢,来个辅助变量游标,根据需求定位游标
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item,end=' ')
            cur = cur.next
        print(' ')

    def add(self,item):
        """头部插入"""
        node = Node(item)
        # self.__head = node # 这样做原来的头节点就丢了,应该先设置新节点,在动头节点
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾插"""
        # if self.__head is Node:
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None: # 到达尾节点即可,如果指向none,则尾节点就丢了,但空链表没有next属性,需要判断一下
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加"""
        if pos<=0:
            self.add(item)
        elif pos >=self.lenth():
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < pos-1:  # 找到插入位置的前一个节点就行
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        if self.is_empty():
            return
        cur = self.__head
        pre_cur = self.__head
        while cur is not None:  # 保证最后一个遍历到
            if cur.item ==item:
                if cur == self.__head: # 第一节点
                    self.__head = cur.next
                else:
                    pre_cur.next = cur.next
                break
            else:
                pre_cur = cur
                cur = cur.next

    def search(self,item):
        # if self.is_empty():
        #     return False  正常情况包含这种特殊情况
        cur = self.__head
        while cur is not None:  # 保证最后一个遍历到
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False



class Nodes:
    def __init__(self,data,next=None,prev=None):
        self.item = data  # 数据区
        self.next = next  # 地址区
        self.prev = prev



class DoubleLinkList:
    def __init__(self,head):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def lenth(self):
        count = 0
        cur = self.__head
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.item,end='')
            cur = cur.next
        print('')

    def add(self,item):
        node = Nodes(item)
        node.next = self.__head
        if node.next is not None: # 非空列表
            node.next.prev = node
        self.__head = node

    def append(self,item):
        node = Nodes(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.lenth():
            self.append(item)
        else:
            node =Nodes(item)
            cur = self.__head
            count = 0
            while count < pos - 1:
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self,item):
        if self.is_empty():
            return
        cur = self.__head
        # prev_cur = cur # 不用在定义前驱节点了 通过cur.prev 就能找到
        while cur is not None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    self.__head.prev = None
                break
            else:
                cur.prev.next = cur.next
                if cur.next is not None: # 不是删除尾节点,尾节点不用管cur.prev了,因为从头节点(链表的标识已经找不到cur了)
                    cur.next.prev = cur.prev

    def search(self,item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False







if __name__ == '__main__':
    pass
    # sll = SingleLinkList()
    # print(sll.is_empty())
    # print(sll.lenth())
    #
    # sll.add(100)
    # print(sll.is_empty())
    # print(sll.lenth())
    # sll.travel()
    #
    # print(100*"*")
    # sll.add(200)
    # print(sll.is_empty())
    # print(sll.lenth())
    # sll.travel()
    #
    # print(100*"*")
    # sll.append(400)
    # sll.travel()
    #
    # print(100*"*")
    # sll.insert(2,300)
    # sll.travel()