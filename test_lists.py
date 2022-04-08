import pytest
from lists import Node, SinglyLinkedList as sll


class TestLists:

    def test_Node_str(self):
        a = Node(1)
        assert str(a) == "1"

    def test_Node_eq(self):
        assert Node(2) == Node(2)

    def test_Node_ne(self):
        assert Node(2) != Node(3)

    def test_SLL_len(self):
        assert len(sll([1, 2, 3])) == 3
        assert len(sll([])) == 0
        assert len(sll([1])) == 1

    def test_SLL_str(self):
        assert str(sll([1, None, 3])) == "1->None->3"
        assert str(sll([1, 2, 3])) == "1->2->3"
        assert str(sll([1])) == "1"
        assert str(sll([])) == ""
        assert str(sll([1, 2])) == "1->2"

    def test_SLL_eq(self):
        assert sll([1, 2, 3]) == sll([1, 2, 3])
        assert sll([]) == sll([])

    def test_SLL_ne(self):
        assert sll([1, 2, 3]) != sll([1, 2, 3, 4])
        assert sll([]) != sll([1])

    def test_SLL_getitem(self):
        assert sll([1, 2, 3])[0] == Node(1)
        assert sll([1, 2, 3])[1] == Node(2)
        assert sll([1, 2, 3])[2] == Node(3)

    def test_SLL_delitem(self):
        a = sll([1, 2, 3])
        del a[0]
        assert a == sll([2, 3])
        b = sll([1, 2, 3])
        b.__delitem__(1)
        assert b == sll([1, 3])
        c = sll([1, 2, 3])
        c.__delitem__(2)
        assert c == sll([1, 2])

    def test_SLL_contains(self):
        assert 1 in sll([0, 1, 3])
        assert None not in sll([])

    def test_SLL_setitem(self):
        a = sll([1, 2, 3])
        a[1] = 5
        assert a[1].val == 5
