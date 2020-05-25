"""
write a doubly linked list, with the following features:

- able to set head/tail
- inserting nodes before/after other nodes + at given position
- remove given nodes and removing nodes with given values
- search for nodes based on values

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time O(1) space
    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_before(self.head, node)

    # O(1) time O(1) space
    def set_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insert_after(self.tail, node)

    # O(1) time O(1) space
    def insert_before(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        # make sure we are not inserting the same node that currently exist
        # this is different from value, you can have separate node instances of the same value
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node

        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    # O(1) time O(1) space
    def insert_after(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert

    # O(n) time O(1) space
    def insert_at_position(self, position, node_to_insert):
        if position == 1:
            self.set_head(node_to_insert)
            return
        position = 1
        current_node = self.head
        while position != node_to_insert:
            if current_node is None:
                self.set_tail(node_to_insert)
                return
            position += 1
            current_node = current_node.next
        self.insert_before(current_node, node_to_insert)

    # O(n) time O(1) space
    def remove_nodes_with_value(self, value):
        current_node = self.head
        while current_node is not None:
            removal_candidate = current_node
            current_node = current_node.next
            if value == removal_candidate.value:
                self.remove(removal_candidate)

    # O(1) time O(1) space
    def remove(self, node):
        # replace head and tail in case we want to remove them
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        # update linkes to prev/next nodes
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # disconnet the given node
        node.next = None
        node.prev = None

    # O(n) time O(1) space
    def contains_node_with_value(self, value):
        current_node = self.head
        while current_node is not None:
            if self.current_node.value == value:
                return True
            current_node = current_node.next
        return False
