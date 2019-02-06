from . import origins

def test_founder():
  who = origins.founder()
  names = who.split()
  first = names[0]
  last  = names[1]
  assert 'Rick'  == first
  assert 'Hovac' == last

def test_established():
  when = origins.established()
  assert 'Not 2004' == when[:8]

