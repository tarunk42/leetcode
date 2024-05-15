from linkedlist.LinkedList import linkedList

def test_add():
    l1 = linkedList()
    l1.add(1)
    l1.add(2)
    l1.add(3)
    assert repr(l1) == "[1, 2, 3]"


def test_search():
    ll = linkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert ll.contains(2) == True
    assert ll.contains(4) == True