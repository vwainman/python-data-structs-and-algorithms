class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class SinglyLinkedList:
    def __init__(self, values: list = None):
        if values is None:
            self.head_node = None
            self.length = None
        elif isinstance(values, list):
            self.head_node = Node()
            self.length = len(values)
            node = self.head_node
            for val in values:
                node.val = val
                node.next = Node()
                node = node.next
        else:
            raise ValueError(f"Invalid values arg {values}")

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head_node
        while node.next is not None:
            yield node
            node = node.next

    def __str__(self):
        return '->'.join(str(node) for node in self.__iter__())

    def __eq__(self, other: 'SinglyLinkedList'):
        if not isinstance(other, SinglyLinkedList) or len(self) != len(other):
            return False
        for node1, node2 in zip(self.__iter__(), other.__iter__()):
            if node1 != node2:
                return False
        return True

    def __ne__(self, other: 'SinglyLinkedList'):
        return not self == other

    def __getitem__(self, key: int):
        if isinstance(key, int):
            node = self._locate_key_node(key, self.head_node)
        elif isinstance(key, slice):
            # TODO
            pass
        else:
            raise TypeError(
                f"Invalid argument {key} of type {type(key)}")
        return node

    def __delitem__(self, key: int):
        if isinstance(key, int) and key != 0:
            prev_node = self._locate_key_node(key - 1, self.head_node)
            node = self._locate_key_node(key, self.head_node)
            prev_node.next = node.next
            del node
        elif isinstance(key, int) and key == 0:
            node = self.head_node
            temp = self.head_node.next
            del node
            self.head_node = temp
        else:
            raise TypeError("Invalid key type")
        self.length -= 1

    def __contains__(self, val: any) -> bool:
        for node in self.__iter__():
            if node.val == val:
                return True
        return False

    def _locate_key_node(self, key: int, node: Node) -> Node:
        key = self._validate_key(key)
        i: int = 0
        while i != key:
            i += 1
            node = node.next
        return node

    def _validate_key(self, key: int) -> int:
        if key < 0:
            key += len(self)
        if key >= len(self) or key < 0:
            raise IndexError(
                f"Index {key} is invalid")
        return key

    def __setitem__(self, key: int, val: any) -> None:
        if isinstance(key, int):
            node = self._locate_key_node(key, self.head_node)
            node.val = val
        else:
            raise TypeError("Invalid argument(s) type")
