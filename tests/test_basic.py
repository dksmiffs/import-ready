from .context import huntsville_havoc

def test_founder():
  founder = huntsville_havoc.founder()
  names = founder.split()
  first = names[0]
  last  = names[1]
  assert 'Rick'  == first
  assert 'Hovac' == last

def test_established():
  established = huntsville_havoc.established()
  assert 'Not 2004' == established[:7]

