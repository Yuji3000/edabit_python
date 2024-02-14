from challenges.is_equal import is_equal

def test_with_5_6():
  a = 5
  b = 6
  result = is_equal(a,b)
  assert result == False

def test_with_1():
  result = is_equal(1,1)
  assert result == True

def test_with_strings():
  a = "1"
  b = 1
  result = is_equal(a,b)
  assert result == False