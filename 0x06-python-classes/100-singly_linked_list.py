#!/usr/bin/python3
"""
create class
"""

class Node:
    """define Node"""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.
        Args:
        data (int): the value of the node
        next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node or value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

"""create SinglyLinkedList class"""
class SinglyLinkedList:
    """define SinglyLinkedList"""
    
    def __init__(self):
        """Sets the necessary attributes for the SinglyLinkedList object."""

        self.head = None
    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None or self.head.data >= value:
            new.next_node = self.head
            self.head = new
        else:
            i = self.head
            while i and i.next_node.data < value:
                i = i.next_node
            new.next_node = i.next_node
            i.next_node = new
    
    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""

        j = ""
        i = self.head
        while i:
            j += str(i.data) + "\n"
            i = i.next_node
        return j
