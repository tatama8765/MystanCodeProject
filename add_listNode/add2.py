"""
File: add2.py
Name:楊
------------------------
TODO:庭瑄
""""""
    This programs gives two nodes and in three node we need to add the number
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    """
    This programs gives two nodes and in three node we need to add the number
    :param l1:
    :param l2:
    :return:
    """
    # give  the new listnode
    l3 = ListNode()
    # to record the node position
    cur = l3
    # This number is over 10 and we need to carry, it will be 0 or 1
    carry = 0
    # To take the variable to record the number
    a = 0
    # To take the variable to record the number
    b = 0
    # This number we need to sum and carry from the left to the right
    while l1 is not None or l2 is not None or carry:
        # take l1 listnode number
        if l1 is not None:
            a = l1.val
        else:
            a = 0
        # take l2 listnode number
        if l2 is not None:
            b = l2.val
        else:
            b = 0
        # we need to add  two number
        sum = a + b + carry
        # it may over 10
        val = sum % 10
        # the carry number
        carry = sum // 10
        # to take the val into the node
        cur.next = ListNode(val)
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
        cur = cur.next

    return l3.next

      


    ############


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
