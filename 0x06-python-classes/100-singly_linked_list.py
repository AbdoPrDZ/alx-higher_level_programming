#!/usr/bin/python3
class Node:
    """
    Node - Linked list node
    """

    def __init__(self, data, next_node=None):
        """
        __init__ - Init the node with data and next node

        Args:
            data (int): The data of node
            next_node (Node|None, optional): The next node. Defaults to None.

        Raises:
            TypeError: if data is not integer
            TypeError: if next node not a None or Node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        elif next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        data.getter - Get the node data

        Returns:
            int: The node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data.setter - Set the node data

        Args:
            value (int): The node data

        Raises:
            TypeError: if value is not integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node.getter - Get node next node

        Returns:
            Node|None: the node next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node.setter - Set the node next node

        Args:
            value (Node|None): The node next node

        Raises:
            TypeError: if value is not a Node or None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList - Singly linked list
    """

    def __init__(self):
        """
        __init__ - Init the linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        sorted_insert - Insert value to linked list

        Args:
            value (int): the next node data
        """
        node = self.__head

        while node:
            if node.data > value:
                break
            prev = node
            node = node.next_node

        next = Node(value, node)

        if node == self.__head:
            self.__head = next
        else:
            prev.next_node = next

    def __str__(self):
        """
        __str__ - The linked list str

        Returns:
            str: The linked list items
        """
        _str = ""
        if self.__head:
            node = self.__head
            while node:
                _str += f"{node.data}"
                if node.next_node:
                    _str += "\n"
                node = node.next_node
        return _str
