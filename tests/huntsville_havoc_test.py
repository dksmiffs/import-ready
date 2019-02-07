""" pytest unit tests for the TestPyPi importable package"""
from huntsville_havoc import founder, established

def test_founder():
    """ unit test huntsville_havoc.founder """
    who = founder()
    names = who.split()
    first = names[0]
    last = names[1]
    assert first == 'Rick'
    assert last == 'Hovac'

def test_established():
    """ unit test huntsville_havoc.established """
    when = established()
    assert when[:8] == 'Not 2004'
