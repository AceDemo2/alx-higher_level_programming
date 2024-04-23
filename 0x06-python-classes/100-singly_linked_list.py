#!/usr/bin/python3

"""
create class
"""


class Node:
    """define Node"""

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with the provided data and optional next node.

        Args:
            data (int): The value of the node.
            next_node (Node): The next Node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
            value (int): The value to set as the data of the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
            value (Node): The next Node to set.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if type(value) is not Node or value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


"""create SinglyLinkedList class"""


class SinglyLinkedList:
    """define SinglyLinkedList"""

    def __init__(self):
        """Initializes a SinglyLinkedList object with no nodes."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the provided value into the linked list in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
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
        """
        Returns a string representation of the linked list, displaying the data of each node.

        Returns:
            str: String representation of the linked list.
        """
        j = ""
        i = self.head
        while i:
            j += str(i.data) + "\n"
            i = i.next_node
        return j

