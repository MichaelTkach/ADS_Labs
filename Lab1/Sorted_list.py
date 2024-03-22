class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SortedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value, flag=True):
        if flag:
            print('The element has been successfully added.\n')
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            cur_node = self.head
            while cur_node and cur_node.value <= value:
                cur_node = cur_node.next
            if cur_node is None:  # Insert at the end
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            elif cur_node.prev is None:  # Insert at the beginning
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:  # Insert in the middle
                node.prev = cur_node.prev
                node.next = cur_node
                cur_node.prev.next = node
                cur_node.prev = node

    def print(self):
        print('Your list:', end=' ')
        cur_node = self.head
        while cur_node and cur_node.next:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        if cur_node:
            print(cur_node.value, end='\n\n')
        else:
            print('List is empty.\n')

    def remove_by_index(self, index, flag=True):
        if index < 0:
            print('Index out of range.\n')
            return
        else:
            cur_node = self.head
            while index > 0 and cur_node:
                cur_node = cur_node.next
                index -= 1
            if cur_node:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                else:
                    self.head = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                else:
                    self.tail = cur_node.prev
                print('The element has been successfully removed.\n')
            else:
                if flag:
                    print('Index out of range.\n')

    def remove_by_value(self, value, flag=True):
        cur_node = self.head
        while cur_node and cur_node.value != value:
            cur_node = cur_node.next
        if cur_node:
            if cur_node.prev:
                cur_node.prev.next = cur_node.next
            else:
                self.head = cur_node.next
            if cur_node.next:
                cur_node.next.prev = cur_node.prev
            else:
                self.tail = cur_node.prev
            if flag:
                print('The element has been successfully removed.\n')
        else:
            if flag:
                print('Value not found.\n')

    def __sub__(self, another_list):
        new_lst = SortedList()
        cur_node = self.head
        while cur_node:
            new_lst.add(cur_node.value, flag=False)
            cur_node = cur_node.next
        node = another_list.head
        while node:
            new_lst.remove_by_value(node.value, False)
            node = node.next
        return new_lst


def main():
    s_list = SortedList()
    s_list.add(5)
    s_list.add(3)
    s_list.add(7)
    s_list.add(1)
    s_list.print()
    s_list.remove_by_index(0)
    s_list.print()
    s_list.remove_by_value(7)
    s_list.print()
    s_list2 = SortedList()
    s_list2.add(3)
    s_list2.add(7)
    s_list2.add(3)
    s_list2.add(1)
    s_list2.print()
    s_list3 = s_list - s_list2
    s_list3.print()


if __name__ == '__main__':
    main()