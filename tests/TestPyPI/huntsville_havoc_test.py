"""pytest unit tests for the import-ready package"""
from huntsville_havoc import Origins

def test_founder():
    """unit test Origins.founder"""
    who = Origins.founder()
    names = who.split()
    first = names[0]
    last = names[1]
    assert first == 'Rick'
    assert last == 'Hovac'

def test_established():
    """unit test Origins.established"""
    when = Origins.established()
    assert when[:8] == 'Not 2004'
